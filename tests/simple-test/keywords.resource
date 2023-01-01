*** Settings ***

Documentation
...    Test from robotframework-pretty_console extension

Keyword Tags
...    kw

Library    SeleniumLibrary


*** Keywords ***

Realizar Operacion
    [Documentation]
    ...    valida el resultado de una expresion
    
    [Tags]
    ...    operaciones

    [Timeout]    5 seconds

    [Arguments]    ${expresion}
    
    ${resultado}=    Evaluate    ${expresion}    

    RETURN    ${resultado}

    [Teardown]    Log To Console    El resultado es: ${resultado}


Keyword de prueba
    Open Browser    https://robotframework.org    gc
    