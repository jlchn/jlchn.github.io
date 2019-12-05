---
layout: default
title: DNS
parent: Troubleshooting
nav_order: 18
has_children: false
---

### check the local DNS server

check the `nameserver` in /etc/resolv.conf
``` bash

cat /etc/resolv.conf 

```

or using `nslookup`, the `Server` and `Address` should be the address of local DNS server, or your configured DNS server.

```
nslookup google.com  
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	google.com
Address: 172.217.194.100
Name:	google.com
Address: 172.217.194.102
Name:	google.com
Address: 172.217.194.139
Name:	google.com
Address: 172.217.194.101
Name:	google.com
Address: 172.217.194.113
Name:	google.com
Address: 172.217.194.138
Name:	google.com
Address: 2404:6800:4003:c04::66

```
### Check the name server record

```
nslookup -type=ns google.com           
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
google.com	nameserver = ns3.google.com.
google.com	nameserver = ns1.google.com.
google.com	nameserver = ns2.google.com.
google.com	nameserver = ns4.google.com.
```

###  Authoritative DNS Server vs  Non-Authoritative DNS Server

Authoritative DNS Server keeps the zone file, however, Non-Authoritative DNS Server only keeps the cache of zone file.

Below means the google.com's zone file are fetched from a 127.0.0.53, which is a copy in 127.0.0.53's cache.
```
nslookup google.com  
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	google.com
Address: 172.217.194.100
```
we can find the DNS server which keep the zone file of google.com by specifying `-type=soa`

```
nslookup -type=soa google.com              
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
google.com
	origin = ns1.google.com
	mail addr = dns-admin.google.com
	serial = 283510722
	refresh = 900
	retry = 900
	expire = 1800
	minimum = 60
```

`ns1.google.com  ` is the DNS server keeping the zone file of google.com

let's try to resolve google.com from `dns-admin.google.com` directly, the reponse is from `Authoritative DNS Server`

```
nslookup  google.com   ns1.google.com     
Server:		ns1.google.com
Address:	216.239.32.10#53

Name:	google.com
Address: 172.217.31.110
Name:	google.com
Address: 2404:6800:4001:80d::200e
```

### SOA Record

The SOA means Start Of Authority. 

The SOA record defines the beginning of the authority DNS zone and specifies the global parameters for the zone. 

Every DNS zone must have an SOA record. 

There is one SOA record per zone.

### NS Record


### A Record