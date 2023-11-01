const typingSpeed = 15

const welcomeMessage = "" +
  "~ Welcome to <b>Code Typer</b>! It's like Vim, once you enter you can't exit :D ^1000\n"

const actionMessage = '<b>test</b>'


var typedWelcomeMessage = new Typed('#initial-message', {
  strings: [welcomeMessage,],
  typeSpeed: typingSpeed,
});

// var typedActionMessage = new Typed('#action-message', {
//     strings: [actionMessage],
//     typeSpeed: typingSpeed,
// });