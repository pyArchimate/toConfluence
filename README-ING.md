# 'toConfluence': Tool to upload Markdown documents in Confluence

## Introduction

'toConfluence' is a tool to upload Markdown or Confluence wiki formatted documents as a Confluence page.
It supports basic formatting syntax, including pictures, links and file attachments.

toConfluence is a command line only tool.  

## Syntax
```
usage: create or update Confluence page using wiki or markdown files
       [-h] [-d DIRECTORY] [-id PAGEID] [-pid PARENTID] [-o] [-k SPACEKEY]
       [-m] [-t] [-v] [-D]
       [file]

positional arguments:
  file                  handle the specified file

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        handle all .wi or .md files in the specified directory
  -id PAGEID, --pageid PAGEID
                        update using page ID instead of file name
  -pid PARENTID, --parentid PARENTID
                        specify the parent page ID
  -o, --OrangeSharing   specify the OrangeSharing as Confluence site and pass
                        the JSESSIONID
  -k SPACEKEY, --spaceKey SPACEKEY
                        specify the Confluence Space key - default is 'EAO'
  -m, --markdown        force to convert file from markdown to Confluence wiki
  -t, --test            test mode - print out debug information
  -v, --version         display the application version
  -D, --Download        Download a page with the title given as argument or
                        referred by "--pageId nnn" argument
```

## Configuration file
A Configuration file enables the default setting of some parameters.
File 'toConfluence.conf' is located under the following location:
- Windows: under the path referred by the 'USERPROFILE' environment variable (e.g. C:\users\<username>)
- Linux: under the home path '~/'

Config file example:

```
PROXY_URL = <ProxyURL>>:8080

[confluence]
    url = https://<confluenceURL>/rest/api/content/
    spaceKey = <SpaceKey>
    parentid = 118120651

[orangesharing]
    url = https://orangesharing.com/rest/api/content/
    spaceKey = CEA
    parentid = 193954419
    email = <my e-mail>>
    JSESSIONID = 
```

## Authentication on Confluence (intranet)
'toConfluence' requires to authenticate yourself on the Office network in order to pass through the firewalls and get access to Confluence.
User password will be asked each time 'toConfluence' is called and is not cached.
It is possible, but not recommended, to set the environment variable PWD to your actual password, should you execute many consecutive uploads.
Don't forget to remove it after the operations.

## Authentication with OrangeSharing
OrangeSharing use Microsoft Azure Active Directory to authenticate users. The 'toConfluence' tool is not yet able to 
fully integrate with Azure Active Directory, so the following workaround is in place:
- Log into OrangeSharing via the web browser.
- When logged,  press F12 or go to the 'Developer Tool' menu. Search for 'https://orangesharing.com' in the cookies list, 
under the Application menu. Copy the JSESSIONID token to the clipboard - past it into the toConfluence.conf file
as shown above, so that the session can be used until token expiration.  
- Start the 'toConfluence' tool with the '-o' option
- If you are on the ING Intranet, you will be asked to enter your CEDS password in order to pass the GIBA Proxy, requiring authentication

## Special features in the document conversion

#### Files & drawings

- If the markdown file includes a reference to an image file in the same directory or in the `images` sub-directory relative to the file path, the image file will also be uploaded as attachment to Confluence
- If the markdown file includes a reference to any file in the sub-directory `files`, the file will be uploaded as attachment to Confluence 

#### Plantuml and Kafka AVRO schema files
- Files with `.puml` extension will be embedded as PlantUML in Confluence, resulting of the display of a PlantUML drawing.
- AVRO schema file with `.avsc` extension will be converted to a PlantUML class representation. Sub-schemas are supported and will be represented as distinct classes with a relation to the parent schema.
 
## Release notes

* version 2.0x
    * use the 'pyCurl' library instead of 'requests' to pass through GIBA authentication
    * calculate md5 hash to document body, file & image attachments to verify whether new version should be uploaded or not
       