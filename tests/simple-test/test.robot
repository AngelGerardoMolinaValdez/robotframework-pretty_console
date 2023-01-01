*** Settings ***

Documentation
...    Test from robotframework-pretty_console extension

Test Tags
...    demo

Metadata    python    3.9.0
Metadata    robot    6.0.1

Library    SeleniumLibrary
Resource    keywords.resource

*** Test Cases ***

Caso de prueba
    [Documentation]
    ...    prueba de extension
    
    [Tags]
    ...    extension_python

    [Timeout]    5 seconds

    [Setup]    Log To Console    Iniciando el flujo

    [Template]    Realizar Operacion

    5 * 10
    20 + 20
    10 - 5

    [Teardown]    Log To Console    Terminando mi flujo



Otro Test Con Otra libreria
    Open Browser    https://robotframework.org    gc
    Keyword de prueba
    Close All Browsers
    IF  ${False}
        Log To Console    no es falso
    
    ELSE IF    ${True}
        Log To Console    es falso

    ELSE
        Log To Console    es falso
        
    END
    
    FOR  ${NUM}  IN RANGE    ${1}    ${3}
        Log To Console    es falso
    
    END

    WHILE  ${True}
        Log To Console    es falso
        BREAK
    END

    Fail    adios

    
    