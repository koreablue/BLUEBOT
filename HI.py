const
Discord = require('discord.js');
const
client = new
Discord.Client();

client.on('ready', () = > {
    console.log('I am ready!');
});

client.on('message', message= > {
if (message.content === 'ping')
{
    message.reply('pong');
}
});

client.login('NzM0Njc4NTI1NDYxOTIxODM1.XxVMvw.nq7CeMwXxFxqvN1EcIjS5a_t79E');