"""Advanced professional visual asset management system for chat applications"""

import hashlib
import requests
from pathlib import Path
from typing import Dict, Optional
from PIL import Image
import uuid


class ChatAssetManager:
    """Professional asset management for chat applications with avatar and media handling."""
    
    def __init__(self):
        self.avatar_cache: Dict[str, str] = {}
        self.upload_dir = Path("uploads")
        self.avatar_dir = self.upload_dir / "avatars"
        self.media_dir = self.upload_dir / "media"
        
        # Create directories
        self.avatar_dir.mkdir(parents=True, exist_ok=True)
        self.media_dir.mkdir(parents=True, exist_ok=True)
        
        # Professional avatar categories for different user types
        self.avatar_categories = {
            'business': 'business,professional,office',
            'casual': 'people,portrait,friendly',
            'tech': 'technology,developer,workspace',
            'creative': 'creative,artist,design'
        }
    
    def get_professional_avatar(self, username: str, category: str = 'business') -> str:
        """Get a professional avatar for a user with fallback options."""
        cache_key = f"{username}_{category}"
        
        if cache_key in self.avatar_cache:
            return self.avatar_cache[cache_key]
        
        try:
            # Generate consistent seed for user
            seed = hashlib.md5(username.encode()).hexdigest()[:8]
            
            # Try Unsplash first
            category_terms = self.avatar_categories.get(category, 'portrait,professional')
            response = requests.get(
                f"https://source.unsplash.com/150x150/?{category_terms}&sig={seed}",
                timeout=5,
                allow_redirects=True
            )
            
            if response.status_code == 200:
                avatar_path = self.avatar_dir / f"{username}_{category}_{seed}.jpg"
                with open(avatar_path, 'wb') as f:
                    f.write(response.content)
                
                # Optimize image
                self._optimize_avatar(avatar_path)
                
                avatar_url = f"/uploads/avatars/{avatar_path.name}"
                self.avatar_cache[cache_key] = avatar_url
                return avatar_url
                
        except Exception as e:
            print(f"Error fetching avatar from Unsplash: {e}")
        
        # Fallback to UI Avatars
        fallback_url = f"https://ui-avatars.com/api/?name={username}&background=0084ff&color=fff&size=150&font-size=0.6"
        self.avatar_cache[cache_key] = fallback_url
        return fallback_url
    
    def _optimize_avatar(self, image_path: Path):
        """Optimize avatar image for web display."""
        try:
            with Image.open(image_path) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize to standard avatar size
                img.thumbnail((150, 150), Image.Resampling.LANCZOS)
                
                # Save optimized version
                img.save(image_path, 'JPEG', quality=85, optimize=True)
        except Exception as e:
            print(f"Error optimizing avatar: {e}")
    
    def save_uploaded_avatar(self, username: str, file_content: bytes, filename: str) -> str:
        """Save and process uploaded avatar."""
        try:
            # Generate unique filename
            file_extension = filename.split('.')[-1].lower()
            if file_extension not in ['jpg', 'jpeg', 'png', 'gif']:
                file_extension = 'jpg'
            
            unique_filename = f"{username}_{uuid.uuid4().hex[:8]}.{file_extension}"
            file_path = self.avatar_dir / unique_filename
            
            # Save original file
            with open(file_path, 'wb') as f:
                f.write(file_content)
            
            # Process and optimize
            self._optimize_avatar(file_path)
            
            avatar_url = f"/uploads/avatars/{unique_filename}"
            self.avatar_cache[username] = avatar_url
            return avatar_url
            
        except Exception as e:
            print(f"Error saving uploaded avatar: {e}")
            return self.get_professional_avatar(username)
    
    def save_media_file(self, file_content: bytes, filename: str, username: str) -> tuple[str, str]:
        """Save media file (images, documents) and return URL and file type."""
        try:
            # Generate unique filename
            file_extension = filename.split('.')[-1].lower()
            unique_filename = f"{username}_{uuid.uuid4().hex[:8]}.{file_extension}"
            file_path = self.media_dir / unique_filename
            
            # Save file
            with open(file_path, 'wb') as f:
                f.write(file_content)
            
            # Determine file type
            file_type = self._get_file_type(file_extension)
            
            # Optimize if it's an image
            if file_type == 'image':
                self._optimize_media_image(file_path)
            
            media_url = f"/uploads/media/{unique_filename}"
            return media_url, file_type
            
        except Exception as e:
            print(f"Error saving media file: {e}")
            return None, None
    
    def _get_file_type(self, extension: str) -> str:
        """Determine file type based on extension."""
        image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'webp']
        document_extensions = ['pdf', 'doc', 'docx', 'txt', 'rtf']
        video_extensions = ['mp4', 'avi', 'mov', 'wmv']
        audio_extensions = ['mp3', 'wav', 'ogg', 'm4a']
        
        if extension in image_extensions:
            return 'image'
        elif extension in document_extensions:
            return 'document'
        elif extension in video_extensions:
            return 'video'
        elif extension in audio_extensions:
            return 'audio'
        else:
            return 'file'
    
    def _optimize_media_image(self, image_path: Path):
        """Optimize media images for chat display."""
        try:
            with Image.open(image_path) as img:
                # Convert to RGB if necessary
                if img.mode not in ['RGB', 'RGBA']:
                    img = img.convert('RGB')
                
                # Resize large images while maintaining aspect ratio
                max_size = (800, 600)
                if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                # Save optimized version
                if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                    img.save(image_path, 'JPEG', quality=85, optimize=True)
                else:
                    img.save(image_path, optimize=True)
                    
        except Exception as e:
            print(f"Error optimizing media image: {e}")
    
    def get_chat_background_images(self) -> Dict[str, str]:
        """Get professional chat background options."""
        backgrounds = {
            'default': 'https://source.unsplash.com/1920x1080/?abstract,minimal,blue',
            'professional': 'https://source.unsplash.com/1920x1080/?office,workspace,clean',
            'nature': 'https://source.unsplash.com/1920x1080/?nature,landscape,calm',
            'geometric': 'https://source.unsplash.com/1920x1080/?geometric,pattern,minimal'
        }
        return backgrounds
    
    def get_emoji_assets(self) -> Dict[str, str]:
        """Get emoji asset URLs for chat enhancement."""
        # In a production app, you might use a proper emoji library
        # For now, we'll use Unicode emojis which are supported by modern browsers
        common_emojis = {
            'smile': '😊',
            'laugh': '😂',
            'heart': '❤️',
            'thumbs_up': '👍',
            'thumbs_down': '👎',
            'fire': '🔥',
            'star': '⭐',
            'check': '✅',
            'cross': '❌',
            'thinking': '🤔'
        }
        return common_emojis


# Global asset manager instance
chat_asset_manager = ChatAssetManager()