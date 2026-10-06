pipeline {
    agent any

    environment {
        IMAGE = "mycompany/payment"
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE:$TAG .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm $IMAGE:$TAG pytest'
            }
        }

        stage('Tag') {
            steps {
                sh 'docker tag $IMAGE:$TAG $IMAGE:${BUILD_NUMBER}'
            }
        }

        stage('Push') {
            steps {
                sh 'echo "Image ready: $IMAGE:${BUILD_NUMBER}"'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop payment || true
                    docker rm payment || true

                    docker run -d \
                      --name payment \
                      -p 8099:8080 \
                      -e APP_VERSION=${BUILD_NUMBER} \
                      -e BUILD_NUMBER=${BUILD_NUMBER} \
                      -e GIT_COMMIT=${GIT_COMMIT} \
                      -e BRANCH_NAME=${BRANCH_NAME} \
                      $IMAGE:${BUILD_NUMBER}

                    echo "Application Version: ${BUILD_NUMBER}"
                    echo "Git Commit: ${GIT_COMMIT}"
                    echo "Docker Image: $IMAGE:${BUILD_NUMBER}"
                    echo "Jenkins Build: ${BUILD_NUMBER}"
                '''
            }
        }
    }
}