# arp_spoof_detect

Simple python script to detect ARP Spoofing attacks on your network.
Extracts ARP entries into a text file then splits data and if the script identifies
duplicate MAC addres, creates a log.txt file, prints duplicate MAC address
and timestamps the event for further investigation.
