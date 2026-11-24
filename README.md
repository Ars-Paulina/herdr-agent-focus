# Agent Focus

A [herdr](https://herdr.dev) plugin that filters the Agents panel to what needs you:

- every agent in the Space you are in, plus
- any agent that is **blocked**, in any Space.

Agents are sorted by attention, then by most recent state change.

herdr forgets Agents panel views when its server stops, so the plugin re-applies the view on every herdr startup.

## Install

```bash
herdr plugin install Ars-Paulina/herdr-agent-focus
```

Requires herdr 0.9.0+ and `python3`. Linux and macOS.

## Use

The view applies automatically on startup. To apply it by hand (for example right after installing), run the **Apply agent focus filter** action, or:

```bash
herdr plugin action invoke agent-focus.apply
```

## Change the filter

Edit the `filter` and `sort` in `set-view.py`. For example, add `"done"` next to `"blocked"` to also show finished agents from other Spaces.

## Uninstall

```bash
herdr plugin uninstall agent-focus
```

The view stays until herdr restarts.
