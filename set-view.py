"""Agents panel filter: current workspace + blocked anywhere. herdr drops the view on server exit;
the plugin's [[startup]] hook runs this again after every start."""
import json, os, socket, sys

req = {"id": "view_set", "method": "agent.view.set", "params": {
    "source": "plugin:" + os.environ["HERDR_PLUGIN_ID"], "label": "focus",
    "filter": {"op": "any", "filters": [
        {"op": "eq", "field": "workspace_id", "value": {"context": "current_workspace_id"}},
        {"op": "in", "field": "status", "values": ["blocked"]}]},
    "sort": [{"field": "attention", "order": "desc"},
             {"field": "state_change_seq", "order": "desc"}]}}

s = socket.socket(socket.AF_UNIX)
s.settimeout(5)
s.connect(os.environ["HERDR_SOCKET_PATH"])
s.sendall((json.dumps(req) + "\n").encode())
r = json.loads(s.makefile().readline())
print(r)
sys.exit(1 if "error" in r else 0)
