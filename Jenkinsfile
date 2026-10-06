pipeline {
    agent any

    environment {
        IMAGE = "mycompany/payment"
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build') {
            steps {
                bat 'docker build -t %IMAGE%:%TAG% .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm %IMAGE%:%TAG% pytest'
            }
        }

        stage('Tag') {
            steps {
                bat 'docker tag %IMAGE%:%TAG% %IMAGE%:release-%BUILD_NUMBER%'
            }
        }

        stage('Push') {
            steps {
                bat 'echo Image ready: %IMAGE%:release-%BUILD_NUMBER%'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    docker stop payment >nul 2>&1
                    docker rm payment >nul 2>&1

                    docker run -d ^
                      --name payment ^
                      -p 8099:8080 ^
                      -e APP_VERSION=%BUILD_NUMBER% ^
                      -e BUILD_NUMBER=%BUILD_NUMBER% ^
                      -e GIT_COMMIT=%GIT_COMMIT% ^
                      -e BRANCH_NAME=main ^
                      %IMAGE%:release-%BUILD_NUMBER%

                    echo ========================================
                    echo       DEPLOYMENT INFORMATION
                    echo ========================================
                    echo Application Version: %BUILD_NUMBER%
                    echo Git Commit: %GIT_COMMIT%
                    echo Branch: main
                    echo Docker Image: %IMAGE%:release-%BUILD_NUMBER%
                    echo Jenkins Build: %BUILD_NUMBER%
                    echo ========================================
                '''
            }
        }
    }
}