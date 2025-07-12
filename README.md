# 📚 Flask Book Manager

A beautiful and responsive web application for managing your personal book collection. Built with Flask backend and modern CSS frontend.

## ✨ Features

- **Add Books**: Easily add new books with title and author
- **Delete Books**: Remove books from your collection
- **Update Books**: Edit book titles with inline editing
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Modern UI**: Beautiful glassmorphism design with smooth animations
- **Real-time Updates**: Instant feedback on all operations

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd flask-book-manager
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
flask-book-manager/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Main HTML template
├── static/
│   └── style.css       # CSS styles
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🛠️ Usage

### Adding a Book
1. Enter the book title in the "Enter book title" field
2. Enter the author name in the "Enter author name" field
3. Click the "Add Book" button

### Updating a Book
1. Find the book you want to update in the list
2. Enter the new title in the "New title" field next to the book
3. Click the "Update" button

### Deleting a Book
1. Find the book you want to delete in the list
2. Click the red "Delete" button next to the book

## 🎨 Design Features

- **Glassmorphism UI**: Modern frosted glass effect
- **Gradient Backgrounds**: Beautiful color transitions
- **Smooth Animations**: Hover effects and transitions
- **Responsive Layout**: Mobile-first design approach
- **Interactive Elements**: Engaging user interactions

## 🔧 Technical Details

### Backend (Flask)
- **Framework**: Flask (Python web framework)
- **Template Engine**: Jinja2
- **HTTP Methods**: GET, POST
- **Data Storage**: In-memory (session-based)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with flexbox and grid
- **Responsive Design**: Mobile-first approach
- **Font**: Inter (Google Fonts)

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Display homepage with book list |
| POST   | `/`      | Add a new book |
| POST   | `/delete` | Delete a book |
| POST   | `/update` | Update book title |

## 🚀 Deployment

### Local Development
```bash
export FLASK_ENV=development
python app.py
```

### Production
For production deployment, consider using:
- **Gunicorn** as WSGI server
- **Nginx** as reverse proxy
- **PostgreSQL** or **MySQL** for persistent storage

## 🔮 Future Enhancements

- [ ] User authentication
- [ ] Book categories and tags
- [ ] Search and filter functionality
- [ ] Book ratings and reviews
- [ ] Cover image support
- [ ] Database persistence
- [ ] Reading progress tracking
- [ ] Import/Export functionality

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports

Found a bug? Please open an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)


## 🙏 Acknowledgments

- Flask documentation and community
- Google Fonts for the Inter font family
- Inspiration from modern web design trends

---

**Happy Reading! 📖✨**
