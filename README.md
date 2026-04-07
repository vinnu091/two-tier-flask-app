# Secure Multi-Tier Application Deployment on AWS EKS

## 📌 Project Overview
This project demonstrates the deployment of a high-availability, secure two-tier web application (**Flask & MySQL**) on a managed **Amazon EKS (Elastic Kubernetes Service)** cluster. The architecture focuses on production-readiness, implementing persistent data layers, automated load balancing, and a "Shift-Left" security strategy. 

The primary goal was to move from a monolithic setup to a cloud-native, containerized environment that handles scaling and self-healing automatically.

---

## 🏗 System Architecture & Traffic Flow

**Traffic Path:**
`User` → `Network Load Balancer (NLB)` → `EKS Worker Nodes` → `Flask Pods` → `MySQL Service (ClusterIP)` → `MySQL Pod` → `Amazon EBS`

---

## 🛠 Tech Stack
* **Cloud:** AWS (EKS, VPC, IAM, EBS, NLB, Route 53)
* **Orchestration:** Kubernetes, Helm
* **Security:** Trivy, SonarQube, IAM Roles for Service Accounts (IRSA)
* **CI/CD:** Jenkins
* **Application:** Flask (Python), MySQL

---

## 🔍 Troubleshooting: The Networking Challenge
During initial deployment, Flask pods faced `503 Service Unavailable` errors because they couldn't reach the MySQL database.

### **The Root Cause:**
* **Security Group Isolation:** Worker nodes were in different subnets, and the default security group blocked port **3306**.
* **DNS Resolution:** The Flask pods couldn't resolve the `mysql-service` internal DNS name.

### **The Fix:**
1. **Security Group Update:** Added a self-referencing rule to the EKS Node Security Group to allow inbound traffic from itself on all ports.
2. **CoreDNS Verification:** Restarted CoreDNS to refresh the internal service discovery mapping.
3. **Validation:** Confirmed connectivity using a `busybox` pod with `nslookup` and `telnet`.

---

## 🛡️ Security Implementation (Shift-Left)
* **Vulnerability Scanning:** Automated **Trivy** scans in the pipeline; builds fail on "Critical" vulnerabilities.
* **Static Analysis:** **SonarQube** gates ensure code quality and credential safety.
* **Least Privilege:** Used **IRSA** to give pods specific permissions to manage EBS volumes without giving full EC2 access.
* **Data Persistence:** Decoupled data using **AWS EBS** to ensure database state survives pod restarts.

---

## 🚀 How to Deploy

### 1. Prerequisites
* AWS CLI configured.
* `kubectl` and `helm` installed.
* An existing EKS Cluster.

### 2. Infrastructure Setup
```bash
# Install the EBS CSI Driver
kubectl apply -k "[https://github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.x](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.x)"

# Deploy Application via Helm
helm install flask-app ./charts/flask-app-chart
