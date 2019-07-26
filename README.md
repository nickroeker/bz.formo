# bz.formo - Bluzelle Formo - An Unofficial Bluzelle Swarm Manager

Bluzelle Formo is a REST API for managing swarms of Bluzelle nodes. It is
named after my favorite "beekeeper" (get it, _swarm manager_?), Eric Formo.

## Notice

This is a personal project that is not even yet in Alpha stage. No API exists,
only skeletons and ideas of what may be.

## Local Installation & Setup

### Via PyPI

Simply `pip install bz.formo` and then `python3 -m bz.formo` to start the
server on port 49999.

### Via Git/Source

```sh
pip install -r requirements.txt -c constraints.txt .
```

## Basic Management

Want a swarm?

```
GET http://localhost:49999/api/v1/browser/newSwarm?numNodes=4
```

Get rid of a swarm?

```
GET http://localhost:49999/api/v1/browser/deleteSwarm?swarmId=yourSwarm
```


Want to be more RESTful?

```sh
POST http://localhost:49999/api/v1/swarms       # Create a swarm
DELETE http://localhost:49999/api/v1/swarms/1   # Delete swarm #1
GET http://localhost:49999/api/v1/swarms        # See all swarms
GET http://localhost:49999/api/v1/swarms/1      # Details swarm #1
```

You can get node info too via `/api/v1/nodes`.
```sh
GET /api/v1/nodes           # List of nodes being managed (may or may not be running)
GET /api/v1/nodes/1         # Node #1 details
GET /api/v1/nodes/1/logs    # Fetch logs for Node #1
```

There are also task endpoints,
```sh
GET /api/v1/tasks/getCores?swarmId=___      # Trigger core collection
GET /api/v1/tasks/getLogs?swarmId=___       # Trigger log collection, gzip'd
GET /api/v1/tasks/getArchive?swarmId=___    # Collect executable, logs, and binary in one compressed archive
```
