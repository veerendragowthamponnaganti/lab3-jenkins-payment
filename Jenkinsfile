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
                bat 'docker tag %IMAGE%:%TAG% %IMAGE%:%BUILD_NUMBER%'
            }
        }

        stage('Push') {
            steps {
                bat 'echo Image ready: %IMAGE%:%BUILD_NUMBER%'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    docker stop payment || exit /b 0
                    docker rm payment || exit /b 0

                    docker run -d ^
                      --name payment ^
                      -p 8099:8080 ^
                      -e APP_VERSION=%BUILD_NUMBER% ^
                      -e BUILD_NUMBER=%BUILD_NUMBER% ^
                      -e GIT_COMMIT=%GIT_COMMIT% ^
                      -e BRANCH_NAME=%BRANCH_NAME% ^
                      %IMAGE%:%BUILD_NUMBER%

                    echo Application Version: %BUILD_NUMBER%
                    echo Git Commit: %GIT_COMMIT%
                    echo Docker Image: %IMAGE%:%BUILD_NUMBER%
                    echo Jenkins Build: %BUILD_NUMBER%
                '''
            }
        }
    }
}