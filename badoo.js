//phantom.injectJs('settings.js');
var casper = require('casper').create();
var mouse = require('mouse').create(casper);
var json = require('badoo.json');
//require('utils').dump(json);
var username=json['username'];
var password=json['password'];
var minratio=json['minratio'];
var lastindx=json['lastindx'];
var unrated =json['unrated'];

var fs     = require('fs');

function saveJSON(){
	//casper.echo('save to JSON...');
	var jsonStr = "{\n";
	jsonStr+= '"username":"'+username+"\",\n";
	jsonStr+= '"password":"'+password+"\",\n";
	jsonStr+= '"minratio":'+minratio+",\n";
	jsonStr+= '"unrated":'+unrated+",\n";
	jsonStr+= '"lastindx":'+lastindx+" \n";
	jsonStr+= '}';
	fs.write('badoo.json', jsonStr, 'w');
	
	//var jsonArray;
	//jsonArray.push($("#firstname").val();
	//jsonArray.push($("#lastname").val();
	//var myJsonString = JSON.stringify(json);
}


	
casper.userAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X)');
//casper.userAgent('Mozilla/6.0 (compatible; MSIE 6.0; Windows NT 5.1)');
casper.start('http://badoo.com', function() {
	phantom.outputEncoding="cp866";
    this.echo(this.getTitle());
	this.capture('badoo-start.png');
});

casper.then(function() {
	var numTimes = 5000, count = lastindx+1;
	var x = require('casper').selectXPath;
	this.echo('Starting..');
	
	this.repeat(100, function() {
		
		this.wait(10000,function(){this.echo('----------- count='+count)});
		this.waitForSelector('div.ovl-frame.js-ovl-wrap',
			function ifFuckingOverlay(){
				this.echo('Поебень всплыла от баду , убираем нах...');	
				this.capture('Overlay10='+count+'.png');
				var sleep = 6000;
				if (this.exists(x('//p[text()="Этот аккаунт используется на другом устройстве."]'))) {
					sleep = 60000;
					this.echo('Этот аккаунт используется на другом устройстве.='+count);	
					this.click('span.b-link.js-continue'); // Жмем продолжить
				}
				else if (this.exists(x('//p[text()="Время сеанса истекло. Пожалуйста, выполните вход ещё раз."]'))) {
					sleep = 60000;
					this.echo('Время сеанса истекло. Пожалуйста, выполните вход ещё раз.'+count);	
					this.click('span.b-link.js-session-expire'); // Жмем продолжить
				}
				//if (this.exists(x('//span[text()="Нет, спасибо"]'))) {
				else if (this.exists(x('//p[text()="У вас закончились голоса. Хотите проголосовать ещё 600 раз сегодня?"]'))) {
					this.echo('У вас закончились голоса='+count);	
					this.echo('Zzzzz... for 60 sec');
					this.wait(60000,function(){
						this.click('i.icon.icon--white.js-ovl-close');
						this.echo('Пиздуем дальше...');
					});
				}
				else if (this.exists(x('//h1[text()="Пусть вас видят чаще"]'))) {
					this.echo('Пусть вас видят чаще='+count);	
					this.click('span.p-link.js-ovl-close');
				}
				else if (this.exists(x('//p[text()="Вы действительно хотите выйти?"]'))) {
					this.echo('Вы действительно хотите выйти?='+count);	
					this.click('span.b-link.js-signout-immediately');
				}
				else {
					// Повысьте свои шансы!
					// Нравится Badoo?
					// О Да! Это взаимно :)
					this.capture('Hren='+count+'.png');
					this.echo('Прочая поебическая всплывающая хрень от баду='+count);
					if (this.exists('i.icon.icon--white.js-ovl-close')) {
						this.click ('i.icon.icon--white.js-ovl-close');
					} 
					else if (this.exists('i.icon.icon--grey.js-ovl-close')){
						this.click      ('i.icon.icon--grey.js-ovl-close');
					}
					else {
						fs.write('ERROR-hren.html', this.getHTML() , 'w');
						this.echo('[ERROR:]Неопознанная поебическая хрень от баду! See ERROR-hren.html');
						this.exit();
					}
				}
				this.echo('Zzzzzz... for '+sleep/1000+' seconds');
				this.wait(sleep,function(){this.echo('Подъем! Пиздуем дальше...')});
				this.waitWhileVisible('div.ovl-frame.js-ovl-wrap',
					function() {
						this.echo('Убрали поебень='+count);
						this.capture('Disapeared='+count+'.png');
					},
					function() {
						this.echo('[ERROR]: А херня не исчезает!',+count);
						this.capture('Error10='+count+'.png');
					},
					5000
				);
				
			},
			function ifCleanBadoo(){
				this.echo('in badoo');
				if (this.exists('span.b-link.js-profile-header-toggle-layout')) {	// главная-странца 
					if (!this.exists('div.profile.profile--info.js-profile-layout-container')){	// если не открыт профайл
						this.echo('click profile button');
						this.click ('span.b-link.js-profile-header-toggle-layout');	// Заходим в профайл
					}
					this.waitForSelector('div.profile.profile--info.js-profile-layout-container',
						function(){
							this.echo('profile opened');
							rating=unrated; 
							if (this.exists('b.scale-value.no-dps')){
								rating=this.fetchText('b.scale-value.no-dps').replace(",",".");
								if (rating==""){
									rating=unrated; 
								}
							}
							this.echo("rating="+rating);
							this.capture("./badoo-game/profile=("+rating+")=["+count+"].png");
							++count;
							lastindx=count;					
							saveJSON();
							if (parseFloat(rating)>minratio){
								this.echo("click yes");
								this.click('span[class="b-link js-profile-header-vote"][data-choice="yes"]');
							}
							else {
								this.echo("click no");
								this.click('span[class="b-link js-profile-header-vote"][data-choice="no"]');
							}
						},
						function(){
							this.echo("Наверно вылезла поебень");
						},
						5000
					);
				}
				else if (this.exists('a.btn.btn--sm.btn--white')){	// start page
					this.echo('Жмем "Войти"')
					this.click ('a.btn.btn--sm.btn--white');	
					this.waitForSelector('form.no_autoloader.form.js-signin',function(){
						this.echo('Authorization...');	
						this.fill('form.no_autoloader.form.js-signin', {
							'email': username, 
							'password': password},
							true);
						this.evaluate(function () {$('form.no_autoloader.form.js-signin').submit(); 	});
					});
				}
				else {
					this.echo("[ERROR:]WTF");
				}
			},
			1000
		)
	});
});
casper.run();

