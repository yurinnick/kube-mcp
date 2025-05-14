import argparse
from .server import mcp


def main():
    """Kube MCP"""
    parser = argparse.ArgumentParser(description="KubeMCP")
    parser.parse_args()
    mcp.run()


if __name__ == "__main__":
    main()
