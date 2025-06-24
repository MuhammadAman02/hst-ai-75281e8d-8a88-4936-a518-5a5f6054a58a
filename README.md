# WhatsApp-Style Chat Application

A modern, real-time chat application built with NiceGUI, featuring WhatsApp-inspired design and professional functionality.

## 🚀 Features

### Core Functionality
- **Real-time Messaging**: Instant message delivery via WebSocket connections
- **User Authentication**: Secure registration and login system
- **Chat Rooms**: Create and join multiple chat rooms
- **Message Persistence**: All messages saved to SQLite database
- **File Attachments**: Upload and share images and files
- **User Avatars**: Professional profile pictures with automatic defaults

### User Experience
- **WhatsApp-Inspired UI**: Modern, familiar chat interface
- **Responsive Design**: Works perfectly on desktop and mobile
- **Online Status**: Real-time user presence indicators
- **Typing Indicators**: See when others are typing
- **Message Status**: Delivery and read receipts
- **Professional Avatars**: Automatic high-quality profile pictures

### Technical Excellence
- **Zero Configuration**: Runs immediately without setup
- **Production Ready**: Containerized deployment with Docker
- **Secure**: Password hashing and session management
- **Optimized**: Efficient image processing and caching
- **Scalable**: Clean architecture for future enhancements

## 🛠️ Quick Start

### Option 1: Direct Python Execution
```bash
# Clone or download the application files
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 2: Docker Deployment
```bash
# Build the container
docker build -t whatsapp-chat .

# Run the container
docker run -p 8080:8080 -v $(pwd)/data:/app/data whatsapp-chat
```

### Option 3: Docker Compose (Recommended)
```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f
```

## 📱 Usage

1. **Access the Application**
   - Open your browser to `http://localhost:8080`
   - You'll see the welcome page with login/register options

2. **Create an Account**
   - Click "Register" to create a new account
   - Fill in username, email, and password
   - Your professional avatar will be automatically generated

3. **Start Chatting**
   - Login with your credentials
   - Create or join chat rooms
   - Start messaging in real-time!

4. **Advanced Features**
   - Upload profile pictures
   - Share files and images
   - Create private or public rooms
   - See online status of other users

## 🏗️ Architecture

### Technology Stack
- **Frontend**: NiceGUI (Python-based reactive UI)
- **Backend**: FastAPI integration with NiceGUI
- **Database**: SQLAlchemy with SQLite
- **Real-time**: WebSocket connections
- **Authentication**: Passlib with bcrypt hashing
- **File Processing**: Pillow for image optimization

### Project Structure
```
whatsapp-chat/
├── main.py                 # Application entry point
├── app/
│   ├── core/
│   │   └── assets.py      # Professional asset management
│   └── static/
│       └── css/
│           └── main.css   # WhatsApp-inspired styling
├── uploads/               # User-generated content
│   ├── avatars/          # Profile pictures
│   └── media/            # Shared files
├── data/                 # Database files
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
└── README.md           # This file
```

### Database Schema
- **Users**: Authentication and profile information
- **ChatRooms**: Room management and metadata
- **Messages**: Message content and relationships
- **RoomMembers**: User-room associations

## 🔧 Configuration

### Environment Variables
Create a `.env` file for custom configuration:

```env
# Database
DATABASE_URL=sqlite:///./chat_app.db

# Security
SECRET_KEY=your-secret-key-here

# Server
HOST=0.0.0.0
PORT=8080
DEBUG=false

# File Upload
MAX_FILE_SIZE=10485760  # 10MB
ALLOWED_EXTENSIONS=jpg,jpeg,png,gif,pdf,doc,docx,txt
```

### Customization Options
- **Avatar Sources**: Modify `AvatarManager` to use different image sources
- **UI Themes**: Update CSS variables for custom color schemes
- **File Types**: Configure allowed file extensions and sizes
- **Room Features**: Add private messaging, admin controls, etc.

## 🚀 Deployment

### Production Deployment
1. **Environment Setup**
   ```bash
   # Set production environment variables
   export DEBUG=false
   export SECRET_KEY=$(openssl rand -hex 32)
   ```

2. **Database Migration**
   ```bash
   # The app automatically creates tables on startup
   # For production, consider using Alembic migrations
   ```

3. **Reverse Proxy** (Recommended)
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:8080;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

### Scaling Considerations
- **Database**: Migrate to PostgreSQL for production
- **File Storage**: Use cloud storage (AWS S3, etc.) for uploads
- **Load Balancing**: Use Redis for session storage across instances
- **Monitoring**: Add logging and health check endpoints

## 🔒 Security Features

- **Password Security**: Bcrypt hashing with salt
- **Session Management**: Secure session handling
- **Input Validation**: Comprehensive data validation
- **File Upload Security**: Type and size restrictions
- **SQL Injection Protection**: SQLAlchemy ORM usage
- **XSS Prevention**: Proper data sanitization

## 🎨 Customization

### UI Customization
- Modify `app/static/css/main.css` for styling changes
- Update color schemes by changing CSS variables
- Add custom themes with different color palettes

### Feature Extensions
- **Voice Messages**: Add audio recording and playback
- **Video Calls**: Integrate WebRTC for video communication
- **Message Reactions**: Add emoji reactions to messages
- **Message Search**: Implement full-text search functionality
- **Push Notifications**: Add browser notifications for new messages

### Integration Options
- **External Authentication**: OAuth with Google, GitHub, etc.
- **Bot Integration**: Add chatbots and automated responses
- **API Extensions**: RESTful API for mobile app integration
- **Webhook Support**: External service integrations

## 📊 Performance

### Optimization Features
- **Image Compression**: Automatic image optimization
- **Lazy Loading**: Efficient message loading
- **Connection Pooling**: Optimized database connections
- **Caching**: Avatar and asset caching
- **Responsive Images**: Multiple image sizes for different devices

### Monitoring
- Health check endpoint at `/health`
- Built-in error logging
- Performance metrics tracking
- Database query optimization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

### Common Issues
1. **Port Already in Use**: Change the port in main.py or use `PORT` environment variable
2. **Database Errors**: Delete `chat_app.db` to reset the database
3. **Avatar Loading**: Check internet connection for Unsplash image fetching
4. **File Upload Issues**: Verify upload directory permissions

### Getting Help
- Check the logs for detailed error messages
- Ensure all dependencies are installed correctly
- Verify Python version compatibility (3.8+)
- Review the configuration settings

## 🎯 Roadmap

### Upcoming Features
- [ ] Mobile app (React Native/Flutter)
- [ ] Voice and video calling
- [ ] Message encryption
- [ ] Advanced admin controls
- [ ] Message scheduling
- [ ] Custom emoji support
- [ ] Integration with external services
- [ ] Advanced search and filtering
- [ ] Message backup and export
- [ ] Multi-language support

---

**Built with ❤️ using NiceGUI and modern Python technologies**

*Ready to deploy and scale for your chat application needs!*