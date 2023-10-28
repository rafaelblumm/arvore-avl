@echo off
rem
rem ### Script auxiliar para criação de imagem docker
rem
    setlocal
    set OLD_CD=%CD%
    cd ..
    call :ConfigureEnv
    call :Build
    call :Run
    goto :End
rem
rem Configurações gerais
:ConfigureEnv
    set DOCKER_IMAGE=avl-tree
    set DOCKER_CONTAINER=avl-tree-container
    set DOCKER_PORTS=8501:8501
    goto :eof
rem
rem Cria a imagem do container
:Build
    echo.
    echo +--------------------------------------------------+
    echo ^|           CRIANDO IMAGEM DO CONTAINER            ^|
    echo +--------------------------------------------------+
    echo.
    docker build -t %DOCKER_IMAGE% .
    goto :eof
rem
rem Levanta o container
:Run
    if not %ERRORLEVEL% equ 0 ( 
        echo.
        echo ** ERRO NA CRIAÇÃO DA IMAGEM DO CONTAINER!
        echo ** SCRIPT SERÁ FINALIZADO.
        echo.
        goto :eof
    )
    echo.
    echo +--------------------------------------------------+
    echo ^|              EXECUTANDO CONTAINER                ^|
    echo +--------------------------------------------------+
    echo.
    docker run --name %DOCKER_CONTAINER% -p %DOCKER_PORTS% -d %DOCKER_IMAGE%
    docker ps -l --format table
    goto :eof
rem
rem Finaliza o script
:End
    cd %OLD_CD%
    endlocal
