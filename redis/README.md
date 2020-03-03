# Redis

## Overview
* redis lưu trữ dữ liệu trực tiếp trên memory, nó được sử dụng như một database, cached and message broker. Nó hỗ trợ các kiểu dữ liệu: strings, hashes, list, sets, sorted sets
* Advantages
  * exceptionally fast: redis rất nhanh có thể xử lý được 110.000 SETs per second, 81.000 GETs per second
  * supports rich data types: redis hỗ trợ nhiều kiểu dữ liệu: strins, hashes, lists
  * Được sử dụng trong một số case: caching, messaging-queuses,...

## Install redis on ubuntu
* Run commands
```
$ sudo apt-get update
$ sudo apt-get install redis-server
```
* Start redis
```
$ redis-server
```
* Check if redis is working
```
$ redis-cli
```

## Install redis manager
* Flowing commands
```
$ sudo snap install redis-desktop-manager
```

# Refs
* https://www.tutorialspoint.com/redis/index.htm