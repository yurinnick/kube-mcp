# kube-mcp
Kubernetes MCP

## Setup

1. Install [Goose CLI](https://block.github.io/goose/docs/quickstart/)
2. Install MCP locally
```
$ uv pip install .
```
3. Configure Goose CLI
```
$ goose configure

This will update your existing config file
  if you prefer, you can edit it directly at /home/yurinnick/.config/goose/config.yaml

┌   goose-configure
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◇  What would you like to call this extension?
│  kube-mcp
│
◇  What command should be run?
│  uv run /global/path/to/kube-mcp/.venv/bin/mcp-kube
│
◇  Please set the timeout for this tool (in secs):
│  300
│
◇  Would you like to add a description?
│  No
│
◇  Would you like to add environment variables?
│  No
│
└  Added kube-mcp extension
```
4. Validate that extention is active
```
$ goose

( O)> What tools do you have?
Let me list out the tools that are currently available to me:

1. **Kubernetes MCP Tools**:
   - `kube-mcp__get_resources` - Get resources of a specific kind in a namespace
   - `kube-mcp__get_resource` - Get a specific resource by kind, name, and namespace
   - `kube-mcp__patch_resource` - Patch a specific resource

Let me also check if there are any additional resources available in the kube-mcp extension:
─── list_resources | platform ──────────────────────────
extension_name: kube-mcp

I can also see there are two resources available in the kube-mcp extension:
- `kube://config`
- `kube://context`

Let me check what information these resources provide:
─── read_resource | platform ──────────────────────────
uri: kube://config
─── read_resource | platform ──────────────────────────
uri: kube://context
```

## Development

1. Activate virtual environment
```
$ .venv/bin/activate
```

2. Run MCP server in dev mode
```
$ uv run mcp dev kube_mcp/server.py
```

