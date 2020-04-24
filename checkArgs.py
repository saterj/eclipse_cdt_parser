#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

id300 = ""

for element in root.findall(".//*storageModule[@moduleId='org.eclipse.cdt.core.settings']"):
    if element.attrib['name'] == argv[2]:
        id300 = element.attrib['id']
        #print(element.attrib['name'] + " is " + element.attrib['id'])

for buildConfig in root.findall(".//*/folderInfo"):
    if id300+'.' == buildConfig.attrib['id']:
        #print(id300 + " (300) is in " + buildConfig.attrib['id'])
        for predef in buildConfig.findall('./toolChain/tool[@command="g++"]/option[@valueType="definedSymbols"]/listOptionValue'):
            if 'LOCATION' in predef.attrib['value']:
                print(sys.argv[1] + ": " + predef.attrib['value'])

root.findall(".//*/folderInfo[@id='cdt.managedbuild.config.gnu.cross.exe.debug.439712262.206394049']/toolChain/tool/option/listOptionValue")
