pipeline {
    agent any

    environment {
        IMAGE = "localhost:5000/mycompany/payment"
        TAG = "${BUILD_NUMBER}"
        RELEASE_TAG = "release-${BUILD_NUMBER}"
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
                bat 'docker tag %IMAGE%:%TAG% %IMAGE%:%RELEASE_TAG%'
            }
        }

        stage('Push') {
            steps {
                bat 'docker push %IMAGE%:%RELEASE_TAG%'
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
                      -e APP_VERSION=%RELEASE_TAG% ^
                      -e BUILD_NUMBER=%BUILD_NUMBER% ^
                      -e GIT_COMMIT=%GIT_COMMIT% ^
                      -e BRANCH_NAME=main ^
                      %IMAGE%:%RELEASE_TAG%

                    echo ========================================
                    echo       DEPLOYMENT INFORMATION
                    echo ========================================
                    echo Application Version: %RELEASE_TAG%
                    echo Git Commit: %GIT_COMMIT%
                    echo Branch: main
                    echo Docker Image: %IMAGE%:%RELEASE_TAG%
                    echo Jenkins Build: %BUILD_NUMBER%
                    echo ========================================
                '''
            }
        }
    }
}