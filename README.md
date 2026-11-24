# Agent Focus

A [herdr](https://herdr.dev) plugin that filters the Agents panel to what needs you:

- every agent in the Space you are in, plus
- any agent that is **blocked**, in any Space.

Agents are sorted by attention, then by most recent state change.

herdr forgets Agents panel views when its server stops, so the plugin re-applies the view on every herdr startup.

Requires herdr 0.9.0+ and `python3`. Linux and macOS.

## Quick start

1. Install the plugin:

   ```bash
   herdr plugin install Ars-Paulina/herdr-agent-focus
   ```

2. Optional: add a keyboard shortcut to herdr's `config.toml`:

   ```toml
   [[keys.command]]
   key = "prefix+alt+a"
   type = "plugin_action"
   command = "agent-focus.toggle"
   description = "toggle agent focus filter"
   ```

3. Apply the config and turn the filter on right away (otherwise it starts on the next herdr start):

   ```bash
   herdr server reload-config
   herdr plugin action invoke agent-focus.apply
   ```

From then on the filter comes back by itself every time herdr starts.

## How to use

| What | Shortcut (from step 2) | Action name | Command |
|---|---|---|---|
| Switch between the focus filter and herdr's normal Agents view | `prefix+alt+a` | Toggle agent focus filter | `herdr plugin action invoke agent-focus.toggle` |
| Re-apply your current choice | — | Apply agent focus filter | `herdr plugin action invoke agent-focus.apply` |

### Toggle the view

- **Focus filter** (default): the current Space's agents plus blocked agents anywhere.
- **Normal view**: herdr's own Agents panel, every agent.

Toggle again to switch back. Your choice is remembered across herdr restarts.

### Change the filter

The filter lives in `set-view.py` (`filter` and `sort`). For example, add `"done"` next to `"blocked"` to also show finished agents from other Spaces.

A GitHub install is replaced on `herdr plugin update`, so to keep your own filter, clone the repo and link your copy instead:

```bash
git clone https://github.com/Ars-Paulina/herdr-agent-focus
herdr plugin uninstall agent-focus
herdr plugin link ./herdr-agent-focus
```

## Update

```bash
herdr plugin update agent-focus
```

## Uninstall

Switch back to the normal view first, then uninstall:

```bash
herdr plugin action invoke agent-focus.toggle   # only if the filter is on
herdr plugin uninstall agent-focus
```

Then remove the shortcut from your `config.toml`. If you skip the toggle, the filter stays until herdr restarts.
