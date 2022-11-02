# Mendeklarasikan Fungsi
nama() {
	echo "Siapa namamu"
	read nama
	npm				# memanggil fungsi didalam fungsi(fungsi bersarang)
}
npm() {
	echo "Sebutkan NPM mu"
	read npm
	echo -e "hai $nama dengan NPM $npm, Selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

# Memanggil fungsi
nama


