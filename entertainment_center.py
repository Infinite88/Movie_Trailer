# Imports
import fresh_tomatoes
import media

'''----- Creates Instances of the class Movie from Media-----'''  
old_republic = media.Movie(
	'Star Wars: The Old Republic', 
	'http://www.loadthegame.com/wp-content/uploads/2014/10/Star-Wars-The-Old-Republic-wallpaper-.jpg', #noqa
	'https://www.youtube.com/watch?v=bVyJP92TiVg', 
	'Massively Multiplayer Online Role-Playing',
	'BioWare')

fallen_empire = media.Movie(
	'Star Wars: Knights of the Fallen Empire',
	'http://i.ytimg.com/vi/bkgzXpKbVGE/maxresdefault.jpg',
	'https://www.youtube.com/watch?v=bkgzXpKbVGE',
	'Massively Multiplayer Online Role-Playing',
	'BioWare')

mass_effect2 = media.Movie(
	'Mass Effect 2',
	'https://upload.wikimedia.org/wikipedia/en/0/05/MassEffect2_cover.PNG',
	'https://www.youtube.com/watch?v=PHCA8tK117c',
	'Massively Multiplayer Online Role-Playing',
	'BioWare')

mass_effect3 = media.Movie(
	'Mass Effect 3',
	'http://www.thatvideogameblog.com/wp-content/uploads/2014/10/mass-effect-3.jpeg', #noqa
	'https://www.youtube.com/watch?v=eBktyyaV9LY',
	'Massively Multiplayer Online Role-Playing',
	'BioWare')

wow_lich_king = media.Movie(
	'World of Warcraft: Wrath of the Lich King',
	'http://media.blizzard.com/wow/media/wallpapers/bosses/lich-king/lich-king-1920x1200.jpg', #noqa
	'https://www.youtube.com/watch?v=BCr7y4SLhck',
	'Massively Multiplayer Online Role-Playing',
	'Blizzard')

wow_cataclysm = media.Movie(
	'World of Warcraft: Cataclysm',
	'http://www.blogcdn.com/www.joystiq.com/media/2010/10/wow-cataclysm-logo-art-530px.jpg', #noqa
	'https://www.youtube.com/watch?v=Wq4Y7ztznKc',
	'Massively Multiplayer Online Role-Playing',
	'Blizzard')

witcher3 = media.Movie(
	'The Witcher 3: Wild Hunt',
	'http://static.cdprojektred.com/thewitcher/media/wallpapers/witcher3/full/witcher3_en_wallpaper_wallpaper_7_1920x1200_1433245916.jpg', #noqa
	'https://www.youtube.com/watch?v=xt_65k-gv1U',
	'Action Role-Playing',
	'CD Projekt RED')

'''------ End of Instances ------'''

# Creates a list of instances to be displayed 
movies = [witcher3, mass_effect2, mass_effect3, wow_lich_king, wow_cataclysm, 
         old_republic, fallen_empire]

# Opens fresh_tomatoes file 
fresh_tomatoes.open_movies_page(movies)