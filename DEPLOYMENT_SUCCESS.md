# 🎉 MHFA Learning Navigator - Deployment Complete!

**Deployment Date:** January 27, 2026
**Status:** ✅ Successfully Deployed
**Region:** us-west-2

---

## 📋 Deployment Summary

Your Mental Health First Aid (MHFA) Learning Navigator chatbot has been successfully deployed to AWS! The backend infrastructure is fully operational and ready to use.

**Total Deployment Time:** ~6 minutes
**Services Deployed:** 15+ AWS services

---

## 🔑 Access Credentials

### Admin Portal Login
- **Email:** hkoneti@asu.edu
- **Temporary Password:** `TempPass123!`
- **Status:** ✅ Account Created (Password change required on first login)

**Note:** You'll be prompted to change your password when you first log in.

---

## 🌐 API Endpoints

### REST API (Admin Dashboard)
```
https://8gy1gg6r12.execute-api.us-west-2.amazonaws.com/prod/
```

**Available Endpoints:**
- `/session-logs` - View chat session logs
- `/escalated-queries` - Manage escalated queries
- `/files` - Document management
- `/user-profile` - User profile management
- `/recommendations` - Get personalized recommendations
- `/presigned-url` - Generate S3 upload URLs

### WebSocket API (Real-time Chat)
```
wss://ok01i8tv8f.execute-api.us-west-2.amazonaws.com
```

---

## 🤖 AWS Bedrock Configuration

### Knowledge Base
- **ID:** `QNX4A7HCYE`
- **Name:** KBLearningNavNavigatorKB75D49381
- **Status:** ✅ Active & Synced
- **Documents Indexed:** 1 sample document

### AI Models Enabled
- ✅ Claude 3.5 Sonnet (Chat responses)
- ✅ Amazon Titan Embeddings (Document vectorization)
- ✅ Amazon Nova Lite (Classification)

---

## 🔐 AWS Cognito (Authentication)

### User Pool
- **Pool ID:** `us-west-2_7g0uevt9j`
- **App Client ID:** `5jtcqorpgvdlpvma3qut8gmbig`
- **Region:** us-west-2

### Authentication Features
- Email/Password authentication
- MFA support ready
- Password policies enforced
- Session management

---

## 📦 AWS S3 Buckets

### Documents Bucket
- **Name:** `mhfa-chatbot-docs-1769547754`
- **Purpose:** Store PDF/TXT/MD documents for the Knowledge Base
- **Auto-Sync:** ✅ Enabled (Lambda triggers on file upload/delete)

**Upload documents:**
```bash
aws s3 cp your-document.pdf s3://mhfa-chatbot-docs-1769547754/pdfs/ --region us-west-2
```

The Knowledge Base will automatically sync when you upload new documents!

---

## 🗄️ DynamoDB Tables

### Session Logs Table
- **Purpose:** Store all chat interactions
- **Features:** TTL enabled, sentiment analysis, session tracking

### User Profile Table
- **Purpose:** Store user preferences and history
- **Features:** Role-based personalization (Instructor/Staff/Learner)

### Escalated Queries Table
- **Purpose:** Track queries requiring human intervention
- **Features:** Status tracking, priority management, email notifications

---

## 📧 Email Configuration (SES)

### Email Receipt
- **Purpose:** Handle email replies to escalated queries
- **Status:** ✅ Configured
- **Admin Email:** hkoneti@asu.edu

**Note:** SES is in sandbox mode. To send emails to non-verified addresses, request production access:
```bash
aws ses request-production-access --region us-west-2
```

---

## ⚙️ Lambda Functions Deployed

| Function | Purpose |
|----------|---------|
| chatResponseHandler | Process chat messages and generate AI responses |
| websocket-handler | Handle WebSocket connections |
| SessionLogsHandler | Store and retrieve session logs |
| EscalatedQueriesFn | Manage escalated queries |
| NotifyAdminFn | Send email notifications to admins |
| FileApiHandler | Handle document uploads/downloads |
| UserProfileFn | Manage user profiles |
| KBSyncFunction | Auto-sync Knowledge Base when documents change |
| UpdateQueryStatusFn | Update escalated query status |
| RetrieveSessionLogsFn | Retrieve session logs by filters |

---

## 🧪 Testing Your Deployment

### 1. Test Knowledge Base Query (using AWS CLI)
```bash
# Query the Knowledge Base
aws bedrock-agent-runtime retrieve \
  --knowledge-base-id QNX4A7HCYE \
  --retrieval-query text="What is Mental Health First Aid?" \
  --region us-west-2
```

### 2. Test Admin API (Health Check)
```bash
curl https://8gy1gg6r12.execute-api.us-west-2.amazonaws.com/prod/
```

### 3. Upload Additional Documents
```bash
# Upload a new document
aws s3 cp my-document.pdf s3://mhfa-chatbot-docs-1769547754/pdfs/ --region us-west-2

# Check ingestion status
aws bedrock-agent list-ingestion-jobs \
  --knowledge-base-id QNX4A7HCYE \
  --data-source-id ANYBGDDWRA \
  --region us-west-2
```

---

## 📊 Monitoring & Logs

### CloudWatch Log Groups
- `/aws/lambda/chatResponseHandler` - Chat processing logs
- `/aws/lambda/websocket-handler` - WebSocket connection logs
- `/aws/lambda/KBSyncFunction` - Knowledge Base sync logs

**View logs:**
```bash
# Tail chat handler logs
aws logs tail /aws/lambda/chatResponseHandler --follow --region us-west-2

# View recent errors
aws logs filter-log-events \
  --log-group-name /aws/lambda/chatResponseHandler \
  --filter-pattern "ERROR" \
  --region us-west-2
```

---

## 💰 Cost Estimate

**Monthly cost for moderate usage (~1000 conversations):**

| Service | Estimated Cost |
|---------|----------------|
| AWS Bedrock (Claude Sonnet) | $30-50 |
| AWS Bedrock Knowledge Base | $10-20 |
| Lambda Functions | $1-5 |
| DynamoDB | $5-10 |
| API Gateway | $3-5 |
| S3 Storage | $1-3 |
| CloudWatch Logs | $2-5 |
| OpenSearch Serverless | $10-15 |
| **Total** | **$62-113/month** |

---

## 🚀 Next Steps

### 1. Access Your Frontend Application ✅
The frontend has been deployed to AWS Amplify!

**Frontend URL:** https://main.d2oynh71n0j3np.amplifyapp.com

**Amplify App Details:**
- App ID: `d2oynh71n0j3np`
- App Name: MHFA-Learning-Navigator
- Branch: main
- Status: ✅ Deployed and Live

**To redeploy the frontend:**
```bash
cd frontend
npm run build
cd build && zip -r ../build.zip .
cd ..

# Create new deployment
aws amplify create-deployment --app-id d2oynh71n0j3np --branch-name main --region us-west-2 > deployment.json
UPLOAD_URL=$(cat deployment.json | python3 -c "import sys, json; print(json.load(sys.stdin)['zipUploadUrl'])")
curl -X PUT "$UPLOAD_URL" --upload-file build.zip -H "Content-Type: application/zip"
JOB_ID=$(cat deployment.json | python3 -c "import sys, json; print(json.load(sys.stdin)['jobId'])")
aws amplify start-deployment --app-id d2oynh71n0j3np --branch-name main --job-id $JOB_ID --region us-west-2
```

### 2. Add More Documents
Upload your MHFA training materials:
```bash
aws s3 sync ./your-documents-folder/ s3://mhfa-chatbot-docs-1769547754/pdfs/ --region us-west-2
```

### 3. Configure Production Email
Request SES production access to send emails to any address:
```bash
aws sesv2 put-account-sending-enabled --enabled --region us-west-2
```

### 4. Set Up Custom Domain (Optional)
- Purchase domain in Route 53
- Create SSL certificate in ACM
- Point API Gateway custom domain to your domain

---

## 🛠️ Useful Commands

### Get All Stack Outputs
```bash
aws cloudformation describe-stacks \
  --stack-name LearningNavigatorFeatures \
  --region us-west-2 \
  --query 'Stacks[0].Outputs' \
  --output table
```

### Check Knowledge Base Status
```bash
aws bedrock-agent get-knowledge-base \
  --knowledge-base-id QNX4A7HCYE \
  --region us-west-2
```

### List All Users
```bash
aws cognito-idp list-users \
  --user-pool-id us-west-2_7g0uevt9j \
  --region us-west-2
```

### Create Additional Admin Users
```bash
aws cognito-idp admin-create-user \
  --user-pool-id us-west-2_7g0uevt9j \
  --username newadmin@example.com \
  --user-attributes Name=email,Value=newadmin@example.com Name=email_verified,Value=true \
  --temporary-password "NewPass123!" \
  --region us-west-2
```

---

## 🐛 Troubleshooting

### Issue: Can't login to admin portal
**Solution:** Verify email is confirmed:
```bash
aws cognito-idp admin-update-user-attributes \
  --user-pool-id us-west-2_7g0uevt9j \
  --username hkoneti@asu.edu \
  --user-attributes Name=email_verified,Value=true \
  --region us-west-2
```

### Issue: Knowledge Base not returning results
**Solution:** Check ingestion status:
```bash
aws bedrock-agent list-ingestion-jobs \
  --knowledge-base-id QNX4A7HCYE \
  --data-source-id ANYBGDDWRA \
  --region us-west-2
```

### Issue: Chat not responding
**Solution:** Check Lambda logs:
```bash
aws logs tail /aws/lambda/chatResponseHandler --follow --region us-west-2
```

---

## 📞 Support

For issues or questions:
- Check CloudWatch Logs for detailed error messages
- Review the [4-COMMAND-DEPLOY.md](4-COMMAND-DEPLOY.md) guide
- AWS Support (if you have a support plan)

---

## 🔄 Updating the Deployment

To update the stack after making code changes:
```bash
cd cdk_backend
npx aws-cdk@latest deploy --all \
  -c githubOwner=local-user \
  -c githubRepo=ncwm-chatbot \
  -c adminEmail=hkoneti@asu.edu \
  --require-approval never
```

---

## 🎯 Summary

✅ Backend infrastructure deployed
✅ Knowledge Base configured and synced
✅ Sample document uploaded and indexed
✅ Admin user created
✅ API endpoints active
✅ Auto-sync enabled for documents
✅ All AWS services operational

**Your MHFA chatbot backend is ready to use!**

---

*Generated: January 27, 2026*
*Stack: LearningNavigatorFeatures*
*Region: us-west-2*
