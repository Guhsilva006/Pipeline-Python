pipeline {
    agent any

    environment {
        // Define o local do ambiente virtual para não "sujar" o sistema
        VENV = ".venv"
    }

   stage('Setup Python') {
            steps {
                echo 'Criando ambiente isolado e instalando dependências...'
                sh '''
                    python3 -m venv $VENV
                    $VENV/bin/pip install pytest
                '''
            }
        }

        stage('Testes Unitários') {
            steps {
                echo 'Executando testes com PyTest...'
                // Se o teste falhar aqui, o Jenkins interrompe o build na hora
                sh '$VENV/bin/pytest test_calculadora.py'
            }
        }

        stage('Build / Empacotamento') {
            steps {
                echo 'Gerando o pacote final do projeto...'
                sh '''
                    mkdir -p dist
                    cp calculadora.py dist/
                    echo "Build finalizado em: $(date)" > dist/build_info.txt
                '''
            }
        }

        stage('Arquivamento') {
            steps {
                echo 'Guardando o artefato no Jenkins...'
                // Isso faz o arquivo aparecer para download na tela do Jenkins
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
            }
        }
    }

    post {
        failure {
            echo 'O código está com erro. Build reprovado!'
        }
        success {
            echo 'Código testado e empacotado com sucesso!'
        }
    }
}
