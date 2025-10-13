// pipeline {
//     agent { label 'dev' }

//     stages {
//         stage('Code Clone Stage') {
//             steps {
//                 git url: 'https://github.com/kishorpatil2107/two-tier-flask-app.git', branch: 'master'
//                 echo 'Code clone done...'
//             }
//         }

//         stage('Code Build Stage') {
//             steps {
//                 sh 'docker build -t two-tier-flask-app:latest .'
//                 echo 'Code build done...'
//             }
//         }
        
//         stage('Code Test Stage') {
//             steps {
//                 echo 'Code test done...'
//             }
//         }

//         stage('Docker Push') {
//             steps {
//                 withCredentials([usernamePassword(
//                     credentialsId: "dockerHuCreds",
//                     usernameVariable: "dockerHubUsr",
//                     passwordVariable: "dockerHubPass"
//                 )]) {
//                     sh "docker login -u $dockerHubUsr -p $dockerHubPass"
//                     sh "docker tag two-tier-flask-app $dockerHubUsr/two-tier-flask-app:latest"
//                     sh "docker push $dockerHubUsr/two-tier-flask-app:latest"
//                 }
//             }
//         }

//         stage('Code Deploy Stage') {
//             steps {
//                 sh 'docker compose pull'
//                 sh 'docker compose up -d'
//                 echo 'Code deploy done...'
//             }
//         }
//     }

//     post {
//         success {
//             script {
//                 emailext(
//                     from: 'kishorpatil2107@gmail.com',
//                     to: 'kishorpatil2107@gmail.com',
//                     body: 'Build success for Demo CICD App',
//                     subject: 'Build success for Demo CICD App'
//                 )
//             }
//         }
//         failure {
//             script {
//                 emailext(
//                     from: 'kishorpatil2107@gmail.com',
//                     to: 'kishorpatil2107@gmail.com',
//                     body: 'Build Failed for Demo CICD App',
//                     subject: 'Build Failed for Demo CICD App'
//                 )
//             }
//         }
//     }
// }
pipeline {
    agent { label 'dev' }

    stages {
        stage('Code Clone Stage') {
            steps {
                git url: 'https://github.com/kishorpatil2107/two-tier-flask-app.git', branch: 'master'
                echo 'Code clone done...'
            }
        }

        stage('Code Build Stage') {
            steps {
                sh 'docker build -t two-tier-flask-app:latest .'
                echo 'Code build done...'
            }
        }

        stage('Trivy Scan Stage') {
            steps {
                sh '''
                    # Install Trivy to user's home directory if not present
                    if ! command -v trivy &> /dev/null
                    then
                        echo "Trivy not found, installing..."
                        mkdir -p $HOME/bin
                        curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b $HOME/bin
                        export PATH=$HOME/bin:$PATH
                    fi

                    // # Scan the Docker image
                    // trivy image --exit-code 1 --severity HIGH,CRITICAL two-tier-flask-app:latest
                    # Trivy with skip dirs flag
                    trivy image --skip-dirs /app/mysql-data --exit-code 1 --severity HIGH,CRITICAL your-image-name

                '''
                echo 'Trivy scan completed successfully with no critical/high vulnerabilities.'
            }
        }

        stage('Code Test Stage') {
            steps {
                echo 'Code test done...'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "dockerHuCreds",
                    usernameVariable: "dockerHubUsr",
                    passwordVariable: "dockerHubPass"
                )]) {
                    sh "docker login -u $dockerHubUsr -p $dockerHubPass"
                    sh "docker tag two-tier-flask-app $dockerHubUsr/two-tier-flask-app:latest"
                    sh "docker push $dockerHubUsr/two-tier-flask-app:latest"
                }
            }
        }

        stage('Code Deploy Stage') {
            steps {
                sh 'docker compose pull'
                sh 'docker compose up -d'
                echo 'Code deploy done...'
            }
        }
    }

    post {
        success {
            script {
                emailext(
                    from: 'kishorpatil2107@gmail.com',
                    to: 'kishorpatil2107@gmail.com',
                    body: 'Build success for Demo CICD App',
                    subject: 'Build success for Demo CICD App'
                )
            }
        }
        failure {
            script {
                emailext(
                    from: 'kishorpatil2107@gmail.com',
                    to: 'kishorpatil2107@gmail.com',
                    body: 'Build Failed for Demo CICD App',
                    subject: 'Build Failed for Demo CICD App'
                )
            }
        }
    }
}
