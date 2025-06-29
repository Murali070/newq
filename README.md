# JARVIS AI Assistant v4.0

A sophisticated AI assistant inspired by Tony Stark's JARVIS, featuring voice control, automation, and a modern web interface.

## 🌟 Features

### 🎤 Voice Recognition & Control
- Advanced speech-to-text with multiple language support
- Natural language command processing
- Continuous listening mode with wake word detection
- Voice profile customization (JARVIS, FRIDAY, etc.)

### 🤖 AI-Powered Responses
- Multiple AI provider support (Groq, Cohere, Gemini)
- Intelligent conversation memory
- Real-time information retrieval
- Context-aware responses

### 🔧 Automation & Control
- Web browser automation
- Application launching and control
- Smart scrolling and navigation
- Multi-platform search operations
- Social media management
- Productivity workflow automation

### 💻 Multiple Interfaces
- **Desktop GUI**: PyQt5-based interface with voice visualizer
- **Web Interface**: Modern React-based UI with responsive design
- **Console Mode**: Command-line interface for headless operation

### 🎨 Advanced Features
- Real-time audio visualization
- Smart content analysis
- Automated research workflows
- Enhanced scroll control
- Chat history management
- Voice profile switching

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- Node.js 16+ (for web interface)
- Modern web browser with speech recognition support

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jarvis-ai/jarvis-assistant.git
   cd jarvis-assistant
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install web dependencies** (optional)
   ```bash
   npm install
   ```

4. **Setup environment**
   ```bash
   python run_jarvis.py --setup
   ```

5. **Configure API keys**
   - Copy `.env.example` to `.env`
   - Add your API keys:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     COHERE_API_KEY=your_cohere_api_key_here
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

### Running JARVIS

**GUI Mode (Recommended)**
```bash
python run_jarvis.py --mode gui
```

**Web Interface**
```bash
python run_jarvis.py --mode web
# or
npm run dev
```

**Console Mode**
```bash
python run_jarvis.py --mode console
```

**Environment Check**
```bash
python run_jarvis.py --mode check
```

## 🎯 Voice Commands

### Basic Commands
- "Open Chrome"
- "Search for artificial intelligence"
- "What's the time?"
- "Play some music"
- "Close Notepad"

### Advanced Automation
- "Open Google and search machine learning"
- "Research quantum computing academically"
- "Open my daily workspace"
- "Start meeting mode"
- "Open all social media"

### Smart Navigation
- "Auto scroll down"
- "Smart scroll to next section"
- "Scroll to main content"
- "Go back"
- "Refresh page"

### AI Assistance
- "Analyze this page"
- "Extract all links"
- "Summarize content"
- "Translate page to Spanish"

## 🏗️ Project Structure

```
jarvis-assistant/
├── backend/                 # Python backend
│   ├── __init__.py
│   ├── config.py           # Configuration management
│   ├── utils.py            # Utility functions
│   ├── chatbot.py          # AI chatbot logic
│   ├── automation.py       # Automation engine
│   ├── model.py            # AI model integration
│   ├── speechtotext.py     # Speech recognition
│   ├── TextToSpeech.py     # Text-to-speech
│   └── RealtimeSearchEngine.py
├── src/                     # React frontend
│   ├── components/         # React components
│   ├── hooks/              # Custom hooks
│   ├── utils/              # Frontend utilities
│   └── types/              # TypeScript types
├── frountend/              # PyQt5 GUI
│   ├── GUI.py              # Main GUI application
│   ├── Graphics/           # GUI assets
│   └── Files/              # GUI data files
├── data/                   # Application data
│   ├── ChatLog.json        # Chat history
│   └── voice/              # Voice recognition files
├── run_jarvis.py           # Main launcher
├── requirements.txt        # Python dependencies
├── package.json            # Node.js dependencies
└── README.md
```

## ⚙️ Configuration

### Environment Variables
```env
# AI Provider API Keys
GROQ_API_KEY=your_groq_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here

# User Configuration
USERNAME=User
ASSISTANTNAME=JARVIS
INPUT_LANGUAGE=en-US

# Voice Settings
VOICE_RATE=0.9
VOICE_PITCH=0.6
VOICE_VOLUME=0.9

# Application Settings
DEFAULT_AI_PROVIDER=groq
DEBUG=false
```

### Voice Profiles
- **JARVIS**: Deep, authoritative voice (default)
- **JARVIS Mark II**: Enhanced cinematic voice
- **FRIDAY**: Efficient and direct
- **ChatGPT**: Warm and conversational
- **Assistant**: Clear and helpful
- **Robotic**: Mechanical and precise

## 🔧 API Integration

### Supported AI Providers
1. **Groq** (Recommended)
   - Fast inference
   - Multiple models available
   - Get API key: [Groq Console](https://console.groq.com)

2. **Cohere**
   - Advanced language models
   - Get API key: [Cohere Dashboard](https://dashboard.cohere.ai)

3. **Google Gemini**
   - Google's latest AI model
   - Get API key: [Google AI Studio](https://makersuite.google.com)

### Adding New Providers
1. Create provider class in `src/services/aiProviders.ts`
2. Implement required methods
3. Add to provider list in `AIService`

## 🎨 Web Interface Features

### Modern UI/UX
- Glassmorphism design
- Neon glow effects
- Smooth animations
- Responsive design
- Dark theme with cyan accents

### Advanced Components
- Real-time voice visualizer
- Chat history management
- Voice profile selector
- Advanced scroll controls
- Status monitoring

### Mobile Support
- Touch-friendly interface
- Responsive layouts
- Orientation handling
- Safe area support

## 🔍 Troubleshooting

### Common Issues

**"No module named 'groq'"**
```bash
pip install groq
```

**"Speech recognition not working"**
- Check microphone permissions
- Ensure browser supports Web Speech API
- Try different browsers (Chrome recommended)

**"PyQt5 import error"**
```bash
pip install PyQt5
# On Linux:
sudo apt-get install python3-pyqt5
```

**"API key not working"**
- Verify API key is correct
- Check API key permissions
- Ensure sufficient credits/quota

### Debug Mode
```bash
python run_jarvis.py --mode gui --debug
```

### Environment Check
```bash
python run_jarvis.py --mode check
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Format code
black .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by Tony Stark's JARVIS from the Marvel Cinematic Universe
- Built with modern AI and web technologies
- Community contributions and feedback

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/jarvis-ai/jarvis-assistant/issues)
- **Discussions**: [GitHub Discussions](https://github.com/jarvis-ai/jarvis-assistant/discussions)
- **Documentation**: [Wiki](https://github.com/jarvis-ai/jarvis-assistant/wiki)

---

**"Sometimes you gotta run before you can walk."** - Tony Stark

Made with ❤️ by the JARVIS Development Team