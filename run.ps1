
Write-Host "Executando testes com pytest..." -ForegroundColor Cyan

pytest tests/ -v

if ($LASTEXITCODE -eq 0) {

    Write-Host "Todos os testes passaram!" -ForegroundColor Green
    
    Write-Host "Construindo imagem Docker..." -ForegroundColor Yellow
    docker build -t song-manager-app .
    
    if ($LASTEXITCODE -eq 0) {

        Write-Host "Build concluído com sucesso!" -ForegroundColor Green
    
        
        Write-Host "Iniciando aplicação no Docker...`n" -ForegroundColor Yellow
        docker run -it --rm -v ${PWD}/app/database:/app/app/database song-manager-app
    } else {
        Write-Host "Erro ao construir imagem Docker" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "Testes falharam! Corrija os erros antes de executar." -ForegroundColor Red
    exit 1
}
