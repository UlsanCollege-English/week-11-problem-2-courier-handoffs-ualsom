# tests/test_hw02.py
import pytest
from hw02.main import bfs_path

def test_basic_path():
    graph = {
        "A": ["B", "C"],
        "B": ["C", "D"],
        "C": ["D"],
        "D": []
    }
    # A -> D shortest path is A -> B -> D
    assert bfs_path(graph, "A", "D") == ["A", "B", "D"]

def test_direct_connection():
    graph = {
        "X": ["Y"],
        "Y": ["Z"],
        "Z": []
    }
    # X -> Y is direct
    assert bfs_path(graph, "X", "Y") == ["X", "Y"]

def test_same_node():
    graph = {
        "P": ["Q"],
        "Q": ["R"]
    }
    # Path from node to itself
    assert bfs_path(graph, "P", "P") == ["P"]

def test_no_path():
    graph = {
        "A": ["B"],
        "B": [],
        "C": ["D"],
        "D": []
    }
    # No path between disconnected nodes
    assert bfs_path(graph, "A", "D") is None

def test_missing_nodes():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": []
    }
    # Source or target missing
    assert bfs_path(graph, "X", "C") is None
    assert bfs_path(graph, "A", "Y") is None
