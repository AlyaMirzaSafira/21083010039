# Mendeklarasikan fungsi
function nama {
	echo "Siapa namamu"
	read nama
}
function npm {
	echo "Sebutkan NPM mu"
	read npm
	echo -e "hai $nama dengan NPM $npm, selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}
# Memanggil Fungsi
nama
npm

