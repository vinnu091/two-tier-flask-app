pipeline {
    // agent { label "dev"};
    agent {label "dev"};
    
    stages{
        stage("Code"){
            steps{
                git url: "https://github.com/LondheShubham153/two-tier-flask-app.git", branch: "master"
            }
        }
        stage("Build & Test"){
            steps{
                sh "docker build . -t flaskapp"
            }
        }
        stage("Push to DockerHub"){
            steps{
                withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker tag flaskapp ${env.dockerHubUser}/flaskapp:latest"
                    sh "docker push ${env.dockerHubUser}/flaskapp:latest" 
                }
            }
        }
        stage("Deploy"){
            steps{
                sh "docker compose up -d"
            }
        }
    }
}









// @Library("Shared") _
// pipeline{
    
//     agent { label "dev"};
    
//     stages{
//         stage("Code Clone"){
//             steps{
//                script{
//                    clone("https://github.com/LondheShubham153/two-tier-flask-app.git", "master")
//                }
//             }
//         }
//         stage("Trivy File System Scan"){
//             steps{
//                 script{
//                     trivy_fs()
//                 }
//             }
//         }
//         stage("Build"){
//             steps{
//                 sh "docker build -t two-tier-flask-app ."
//             }
            
//         }
//         stage("Test"){
//             steps{
//                 echo "Developer / Tester tests likh ke dega..."
//             }
            
//         }
//         stage("Push to Docker Hub"){
//             steps{
//                 script{
//                     docker_push("dockerHubCreds","two-tier-flask-app")
//                 }  
//             }
//         }
//         stage("Deploy"){
//             steps{
//                 sh "docker compose up -d --build flask-app"
//             }
//         }
//     }

// post{
//         success{
//             script{
//                 emailext from: 'mentor@trainwithshubham.com',
//                 to: 'mentor@trainwithshubham.com',
//                 body: 'Build success for Demo CICD App',
//                 subject: 'Build success for Demo CICD App'
//             }
//         }
//         failure{
//             script{
//                 emailext from: 'mentor@trainwithshubham.com',
//                 to: 'mentor@trainwithshubham.com',
//                 body: 'Build Failed for Demo CICD App',
//                 subject: 'Build Failed for Demo CICD App'
//             }
//         }
//     }
// }
