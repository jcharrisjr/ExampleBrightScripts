# Examples of command line entries for repeaters, scans, integrations, etc

https://github.com/NeuraLegion/nexploit-cli

## Installing and running a repeater

There are a few different ways to install them on a local asset:

 - npm install

    `sudo apt-get install nodejs npm`

    `sudo npm install -g @neuralegion/nexploit-cli --unsafe-perm=true`
    
    `nexploit-cli repeater --id g31NbaebCRsHdMH3J3gifX --token $BRIGHT_API`
    
 - Docker container

    https://hub.docker.com/r/neuralegion/repeater
    
    `docker pull neuralegion/repeater`
    
    `sudo docker run -it neuralegion/repeater repeater --id g31NbaebCRsHdMH3J3gifX --token $BRIGHT_API`
    
 - Download, install, and run the precompiled binary executable

    https://github.com/NeuraLegion/nexploit-cli/releases/latest

    `nexploit-cli repeater --id g31NbaebCRsHdMH3J3gifX --token $BRIGHT_API`
    
## Running Integration Repeater

Integrations for local ticketing systems can traffic communication through the repeater.

    nexploit-cli integration --access-key $JIRA_ACCESS_KEY --base-url http://192.168.68.222:8080/ --user jharris --password Jira_123 --token $BRIGHT_API
