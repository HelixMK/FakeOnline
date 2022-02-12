const SteamUser = require('steam-user');
const SteamTotp = require('steam-totp');
const fs = require('fs');
const {promisify} = require('util');

const getTicket = (accountName, password, twoFactorCode, appid) => {
	return new Promise((resolve, reject) => {
		const client = new SteamUser();

		client.logOn({
			accountName,
			password,
			twoFactorCode,
		});

		client.on('loggedOn', (details) => {
			console.log(details.client_supplied_steamid);
			client.setPersona(SteamUser.EPersonaState.Online);
			client.gamesPlayed(appid, true);
			client.cancelAuthTicket(appid,console.log);
			client.getAuthSessionTicket(appid, (err, ticket) => {
				if(err) return reject(err);

				fs.writeFile(details.client_supplied_steamid, ticket, (err) => {
					if (err) throw err;
					console.log(details.client_supplied_steamid,' saved!');
				});

				resolve({
					accountId: details.client_supplied_steamid.low,
					ticket,
				});
			});
			
		});

		client.on('error', reject);
	});
};

const getSteamGuardCode = sharedSecret => {
	return promisify(SteamTotp.getTimeOffset)().then(offset => {
		return SteamTotp.generateAuthCode(sharedSecret, offset);
	});
};

/**
 *
 * @param {string} accountName
 * @param {string} password
 * @param {string} secondFactor - Steam Guard Code or shared_secret
 * @param {number} appid
 * @return {Promise<{accountId: number, ticket: Buffer}>}
 */
eblan = async (accountName, password, secondFactor, appid) => {
	if(secondFactor.length > 5) {
		secondFactor = await getSteamGuardCode(secondFactor);
	}

	return await getTicket(accountName, password, secondFactor, appid);
};


eblan(process.argv[2],process.argv[3], '', 4000).then(({ticket}) => {
	//console.log(ticket);
	console.log(ticket.toString('hex'));
	//process.exit(0);
}, err => {
	console.error(err.stack || err);
	//process.exit(1);
});

const request = require('request');
