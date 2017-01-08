//phantom.injectJs('settings.js');
var casper = require('casper').create();
var json = require('badoo.json');
//require('utils').dump(json);
var username=json['username'];
var password=json['password'];
var minratio=json['minratio'];
var lastindx=json['lastindx'];

var fs     = require('fs');

function saveJSON(){
	casper.echo('save to JSON...');
	var jsonStr = "{\n";
	jsonStr+= '"username":"'+username+"\",\n";
	jsonStr+= '"password":"'+password+"\",\n";
	jsonStr+= '"minratio":'+minratio+",\n";
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
	this.capture('badoo-00.png');
	this.click('a.btn.btn--sm.btn--white');
	this.capture('badoo-01.png');
	
	//lastindx+=1;
	//saveJSON();

});




casper.then(function() {
	this.echo('[01] Waiting for login...');
	this.capture('badoo-10.png');
	//*[@id="anketa"]
	//test.assertExists('form[id="anketa"]', "main form is found");
	//this.fill('form[id="anketa"]', {
    //    dlg_login_log: "qwe",
    //     dlg_login_pas: "qwe"
    // }, true);
	 
	//this.fillSelectors('form#user-login', {
    //    'input[name = name ]' : 'abc@gmail.com',
    //    'input[name = pass ]' : 'pwd'
    //}, true);
	//this.waitForSelector("form input[name='login']", function() {
	//	this.fillSelectors('form#user-login', {
	//		'input[name = login]' : 'abc@gmail.com',
	//		'input[name = password ]' : 'pwd'
    //}, true);
	//casper.waitForSelector('form', function(){
	//	this.fill('form', {
	//		'login': 'abc@gmail.com', 
	//		'password': 'pwd'},
	//		true);
	//});
	//this.echo('I am out of selector');
	
	
	this.waitForSelector('form', function(){
		this.fill('form.no_autoloader.form.js-signin', {
			'email': username, 
			'password': password},
			true);
	});
		
	this.capture('badoo-11.png');
	
	//this.click('input.button.login');
	
	//#dlg_login > ul.reset.line.lab_w43 > li:nth-child(4) > div > button
	
	
});

casper.then(function() {
	this.echo('submit');
	this.evaluate(function () {
        $('form.no_autoloader.form.js-signin').submit();
    });
	
	
	this.capture('badoo-20.png');

});	

casper.then(function() {
	
	//body > div.height_full > div.head > div > ul > li:nth-child(1) > a
	
	this.echo('preexit');
	this.wait(10000,function(){
		this.echo('exit');
		this.capture('badoo-exit.png');
	});
	//this.waitForSelector('div.height_full', function(){
	//	this.echo('exit');
	//	this.capture('badoo-30.png');
	//});
});	

casper.then(function() {
	var numTimes = 5000, count = lastindx+1;
	var x = require('casper').selectXPath;
	this.echo('..');
	//this.waitTimeOut(2000);
	var novoice=false;
	this.repeat(numTimes, function() {
		//this.echo('.');
		
		//this.wait(1000,function(){
			//this.echo('wait for love..');
			
			//#mm_cc > section > div.big-photo__gallery > div > section > div
			//this.waitWhileVisible('span.b-link.js-profile-header-vote', 
			//function(){
				//this.waitForSelector('div.big-photo__gallery', function(){
				//----------- Ловим overlay ------------
				//<div class="ovl-frame js-ovl-wrap"> top level
				//this.waitForSelector('div.ovl-frame.js-ovl-wrap', function(){
				//	this.echo('Overlay detected='+count);	
				//});
				//if (this.exists('div.ovl-frame.js-ovl-wrap')){
				//<html lang="ru" dir="ltr" class="js chrome ovl-fading ovl-opened">
				//<div class="ovl-frame js-ovl-wrap">
		this.echo('-----------');
		this.echo('count='+count);
		//if (!this.exists('div.ovl-frame.js-ovl-wrap')){
			
		//var fname = 'page='+count+'.html';
		//fs.write(fname, this.getHTML() , 'w');
		//if (!this.exists('html.js.safari.ovl-fading')){
			//if (novoice==false) {
			//this.echo('I like '+count);
			//this.capture('badoo='+count+'.png');
			//var fname = 'page='+count+'.html';
			//fs.write(fname, this.getHTML() , 'w');
				//++count;
			//}
			//this.echo('I Click yes whitout capture'+count);
			
			//novoice=false;
		//}//}
		//if (this.exists('html.js.safari.ovl-fading')){
		//	this.echo('HTML Overlay detected='+count);	
		//}
		//if (!this.exists('html.js.safari.ovl-fading')){
		// проверяем второй раз , что не появился оверлей
		//if (!this.exists('div.ovl-frame.js-ovl-wrap')){
		if (!this.exists('html.js.safari.ovl-fading')){
			
			var rating="0";
			this.echo("Enter profile...");
			this.waitForSelector('span.b-link.js-profile-header-toggle-layout', function(){
				this.echo('click profile');
				this.click('span.b-link.js-profile-header-toggle-layout');
				this.echo('Whaiting for profile...');
				//this.waitForSelector('div.score-user',function(){
				//	this.echo("rating");
				//});
				//this.waitForSelector('div.score-user',
				this.waitForSelector('b.scale-value.no-dps',
					function(){
						//this.capture('profile='+count+'-profileYes.png');
						rating=this.fetchText('b.scale-value.no-dps').replace(",",".");
						this.echo('Rating= '+rating);
						if (rating==""){
							rating="10";
						}
					},
					function(){
						//this.capture('badoo='+count+'-profileNo.png');
						rating="10";
						this.echo("No rating");
						//this.capture("profile_fail="+count+".png");
					},
					5000
				);
			});
			this.then(function(){
				this.echo("rating="+rating);
				//this.echo("profile_OK");
				lastindx=count;
				this.capture("./badoo-game/profile=("+rating+")=["+count+"].png");
				saveJSON();
				//this.waitForSelector('span.b-link.js-profile-header-vote', 
				this.waitForSelector('span[class="b-link js-profile-header-vote"]', 
					function(){
						//#app_c > div > div.profile__header.js-profile-header-container.js-core-events-container > header > div > div.profile-header__btn.js-profile-header-buttons > div.btn-game.btn-game--hot.js-profile-header-vote-yes.tooltip-wrap
						//#app_c > div > div.profile__header.js-profile-header-container.js-core-events-container > header > div > div.profile-header__btn.js-profile-header-buttons > div.btn-game.btn-game--hot.js-profile-header-vote-yes.tooltip-wrap > span
						//<span class="b-link js-profile-header-vote" data-choice="yes"></span>
						//this.click('div.btn-game.btn-game--hot.js-profile-header-vote-yes.tooltip-wrap.b-link.js-profile-header-vote');
						
						
						//this.click('span.b-link.js-profile-header-vote'); 
						this.echo(rating);
						//var x=rating.replace("0","r");
						//this.echo(x);
						var s = rating;//"the,batter,hit the ball with the bat";
		
						if (parseFloat(rating)>minratio){
							this.echo("click yes")
							this.click('span[class="b-link js-profile-header-vote"][data-choice="yes"]');
						}
						else {
							this.echo("click no")
							this.click('span[class="b-link js-profile-header-vote"][data-choice="no"]');
						}
						++count;
						this.echo('10 sec Zzzz...');
						this.wait(10000,function(){
							this.echo('Wakeup...');
						});
					},
					function(){
						this.echo('No like button...');
					},
					5000
				);
			});
		}
		else {
		//this.waitForSelector('div.ovl-frame.js-ovl-wrap', 
			this.echo('Overlay detected='+count);	
			this.capture('Overlay10='+count+'.png');
			//this.capture('Overlay11='+count+'.png');
			//this.capture('Overlay12='+count+'.png');
			//this.waitWhileVisible('div.ovl-frame.js-ovl-wrap', 
			
			// Пусть вас видят чаще
			this.waitForSelector('span.p-link.js-ovl-close', 
				function(){
					this.echo('span.p-link.js-ovl-close SELECTOR='+count);	
					if (this.exists(x('//span[text()="Нет, спасибо"]'))) {
						this.echo('Нет, спасибо='+count);	
						this.click('span.p-link.js-ovl-close');
					}
				},
				function() {
					this.echo('No 3000='+count);
				},
				3000
			);
			
			// <i class="icon icon--white js-ovl-close">  [Close icon]
			this.waitForSelector('i.icon.icon--white.js-ovl-close', 
				function () {
					this.echo('[SELECTOR] i.icon.icon--white.js-ovl-close ='+count);	
					if (this.exists(x('//p[text()="У вас закончились голоса. Хотите проголосовать ещё 600 раз сегодня?"]'))) {
						--count;
						this.echo('У вас закончились голоса='+count);	
						this.echo('ZZZzzzzz....10 min, --count='+count);	
						novoice=true;
						
						this.wait(600000,
							function(){	
								this.click('i.icon.icon--white.js-ovl-close');
							}
						);
					}
					// <h1>Повысьте свои шансы!</h1>
					else if (this.exists(x('//h1[text()="Повысьте свои шансы!"]'))) {
						this.echo('Повысьте свои шансы! ='+count);	
						this.click('i.icon.icon--white.js-ovl-close');
					}
					else if (this.exists(x('//h1[text()="Нравится Badoo?"]'))) {
						this.capture('Nra='+count+'.png');
						this.echo('Нравится Badoo! ='+count);	
						this.click('i.icon.icon--white.js-ovl-close');
					}
					else {
						this.capture('Hren='+count+'.png');
						this.echo('У вас какая то хрень='+count);
						this.click('i.icon.icon--white.js-ovl-close');
					}
				},
				function() {
					this.echo('No 3001='+count);
				},
				3001
			);
			
			this.waitForSelector('div.ovl-frame.js-ovl-wrap',
				function() {
					this.echo('[SELECTOR] div.ovl-frame.js-ovl-wrap ='+count);	
					if (this.exists(x('//p[text()="Этот аккаунт используется на другом устройстве."]'))) {
						--count;
						this.echo('Этот аккаунт используется на другом устройстве.='+count);	
						this.echo('ZZZzzzzz....10 min, --count='+count);	
						novoice=true;
						
						this.wait(600000,
							function(){	
								this.echo('Жмем продолжить...');	
								this.click('span.b-link.js-continue'); // Жмем продолжить
							}
						);
					}
					else if (this.exists(x('//p[text()="Время сеанса истекло. Пожалуйста, выполните вход ещё раз."]'))) {
						--count;
						this.echo('Время сеанса истекло. Пожалуйста, выполните вход ещё раз.'+count);	
						this.echo('ZZZzzzzz....1 min, --count='+count);	
						novoice=true;
						
						this.wait(60000,
							function(){	
								this.echo('Жмем продолжить...');	
								this.click('span.b-link.js-session-expire'); // Жмем продолжить
							}
						);
					}
					else {
						this.capture('Hren='+count+'.png');
						this.echo('У вас какая то хрень 2='+count);
					}
				},
				function() {
					
				},
				3002
			);
			
			this.waitWhileVisible('div.ovl-frame.js-ovl-wrap',
				function() {
					this.echo('Overlay Disapeared='+count);
					this.capture('Disapeared='+count+'.png');
					this.wait(2000,function(){'Sleep after disapeared'});
				},
				function() {
					this.echo('[PROBLEM]: Overlay dows not disapeared!',+count);
					this.capture('Error10='+count+'.png');
				},
				10000
			);
		}
		this.echo("End repeat");
		
	});
	
});

casper.run();


//	//<span class="p-link js-ovl-close">Нет, спасибо</span>
			//	if (this.exists('span.p-link.js-ovl-close')) {
			//		if (this.exists(x('//span[text()="Нет, спасибо"]'))) {
			//			this.echo('Нет, спасибо='+count);	
			//			this.click('span.p-link.js-ovl-close');
			//			this.waitUntilVisible('span.p-link.js-ovl-close', function() {
			//				this.echo('Нет, спасибо Disapeared!');
			//			});
            //
			//			//this.wait(3000,function(){
			//			//	this.echo('Closed ovl in 3 sec');	
			//			//});
			//		}
			//	}
            //
			//	if (this.exists('i.icon.icon--white.js-ovl-close')) {
			//		if (this.exists(x('//p[text()="У вас закончились голоса. Хотите проголосовать ещё 600 раз сегодня?"]'))) {
			//			this.echo('У вас закончились голоса='+count);	
			//			this.echo('ZZZzzzzz....10 min');	
			//			this.click('i.icon.icon--white.js-ovl-close');
			//				this.wait(600000,function(){
			//				this.echo('Closed ovl in 10 min');	
			//			});
			//		}
			//		// <h1>Повысьте свои шансы!</h1>
			//		else if (this.exists(x('//h1[text()="Повысьте свои шансы!"]'))) {
			//			this.echo('Повысьте свои шансы! ='+count);	
			//			this.click('i.icon.icon--white.js-ovl-close');
			//		}
			//		else {
			//			this.echo('У вас какая то хрень='+count);
			//			this.click('i.icon.icon--white.js-ovl-close');
			//		}
			//		this.wait(3000,function(){
			//			this.echo('Closed ovl in 3 sec');	
			//		});
			//	}
            //
			//	//<div class="btn btn--blue"> 
			//	//	<span class="btn-txt">Продолжить</span> 
			//	//	<span class="b-link js-continue"></span> 
			//	//</div>
			//	
		    //
			//	//this.waitForSelector('i.icon.icon--white.js-ovl-close', 
			//	//	function(){
			//	//		this.capture('overlay='+count+'.png');
			//	//		var x = require('casper').selectXPath;
			//	//		
			//	//		if (this.exists(x('//p[text()="У вас закончились голоса. Хотите проголосовать ещё 600 раз сегодня?"]'))) {
			//	//			this.echo('У вас закончились голоса='+count);	
			//	//			this.echo('ZZZzzzzz....');	
			//	//			this.wait(60000,function(){
			//	//				this.echo('Wake up!');	
			//	//			});
			//	//		}
			//	//		else {
			//	//			this.echo('У вас какая то хрень='+count);
			//	//		}
			//	//		this.click('i.icon.icon--white.js-ovl-close');
			//	//		//this.echo('Повысьте свои шансы! '+count);
			//	//	}, 
			//	//	function (){
			//	//		this.echo('I like '+count);
			//	//		this.capture('badoo='+count+'.png');
			//	//		this.click('span.b-link.js-profile-header-vote');
			//	//		++count;
			//	//		//this.echo('my timeout');
			//	//	},1000);
			//	////this.echo('end wait for overlay..');
			//	//else {
			//	//}
			//});
			//this.then(function() {
			//	this.capture('badoo='+count+'.png');
			//	this.echo('I like '+count);
			//	this.capture('badoo='+count+'.png');
			//	this.click('span.b-link.js-profile-header-vote');
			//	++count;
			//});
			//this.echo('end wait for love..');
			
//			<div class="ovl-frame js-ovl-wrap"><div class="js-ovl-content"> <div class="ovl-body"> <div class="ovl-content">  <h1>Нравится Badoo?</h1> <p> Поставьте нам хорошую оценку :)          </p>   <div class="stars">  <i class="stars__star js-star" data-star-value="1"></i>  <i class="stars__star js-star" data-star-value="2"></i>  <i class="stars__star js-star" data-star-value="3"></i>  <i class="stars__star js-star" data-star-value="4"></i>  <i class="stars__star js-star" data-star-value="5"></i>  <span class="blocker"></span> </div> </div> <div class="ovl-close"><i class="icon icon--grey js-ovl-close"><svg class="icon-svg"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#icon-cross"></use></svg></i></div> <div class="blocker blocker--light"></div> </div> </div><div class="loader loader--lg loader--black ovl-frame-loader"><span class="loader_"></span></div></div>
			