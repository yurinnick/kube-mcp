import json

from kubernetes import config, client, dynamic
from kubernetes.client import api_client
from kubernetes.dynamic.client import ApiException
from mcp.server.fastmcp import FastMCP

KUBERNETES_API_VERSION: str = "v1"

config.load_kube_config()

mcp = FastMCP("KubeMCP")
kube_client = client.CoreV1Api()
dyn_client = dynamic.DynamicClient(api_client.ApiClient())


@mcp.resource("kube://config")
async def get_config() -> str:
    config_data, _ = config.list_kube_config_contexts()
    return json.dumps(config_data)


@mcp.resource("kube://context")
async def get_context() -> str:
    _, active_context = config.list_kube_config_contexts()
    return json.dumps(active_context)


@mcp.tool()
async def get_resources(
    kind: str,
    namespace: str,
) -> str:
    return await get_resource(kind=kind, namespace=namespace, name=None)


@mcp.tool()
async def get_resource(
    kind: str,
    namespace: str,
    name: str,
) -> str:
    return await get_generic_resource(kind, namespace, name)


async def get_generic_resource(kind, namespace, name):
    resource_client = get_resource_client(kind)
    try:
        resp = resource_client.get(
            namespace=namespace,
            name=name,
            async_req=True,
        )
    except ApiException as e:
        return f"ERROR: {e.status} - {e.reason}"

    if name:
        return json.dumps(resp.to_dict())

    return json.dumps([item.to_dict() for item in resp.items])


@mcp.tool()
def patch_resource(
    kind: str,
    name: str,
    namespace: str,
    patch: dict,
) -> str:
    resource_client = get_resource_client(kind)
    resp = resource_client.patch(
        name=name,
        namespace=namespace,
        body=patch,
    )
    return json.dumps(resp)


def get_resource_client(kind: str):
    return dyn_client.resources.get(
        api_version=KUBERNETES_API_VERSION,
        kind=kind,
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
