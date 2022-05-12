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
    
## Running Integration from CLI

Integrations for local ticketing systems can traffic communication through the repeater.

    nexploit-cli integration --access-key $JIRA_ACCESS_KEY --base-url http://192.168.68.222:8080/ --user jharris --password Jira_123 --token $BRIGHT_API

##  Example Running Scan from CLI

    nexploit-cli scan:run --token $BRIGHT_API --name "http://demo.testfire.net/" --crawler http://demo.testfire.net/ --project XXXXXXXXXXXXXXXXX --smart --param query fragment body artifical-query artifical-fragment --module dast --test jwt broken_saml_auth brute_force_login common_files cookie_security csrf xss default_login_location directory_listing dom_xss email_injection file_upload full_path_disclosure header_security html_injection http_method_fuzzing improper_asset_management insecure_tls_configuration ldapi lfi nosql open_buckets open_database osi proto_pollution rfi secret_tokens ssti server_side_js_injection ssrf sqli unvalidated_redirect version_control_systems wordpress xxe xpathi business_constraint_bypass date_manipulation id_enumeration mass_assignment retire_js
