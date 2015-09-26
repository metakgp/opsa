|**time**|  *user*| text| 
|-----------------|-----------------|----------------------------------------------| 
|**09/14/15 18:51**|  *nuwanda*| <@U0AHU8RU0 nuwanda> has joined the channel| 
|**09/14/15 18:51**|  *nuwanda*| <@U0AHU8RU0 nuwanda> set the channel purpose: Ideas that we think will will get a lot of eyeballs for metakgp. But most importantly, are cool.| 
|**09/14/15 18:56**|  *dementor*| <@U0AKGKRST dementor> has joined the channel| 
|**09/14/15 18:56**|  *dementor*| Drone Videos :smile:| 
|**09/14/15 18:57**|  *dementor*| 3D Augmented Tour of Campus -&gt; Floor Wise Maps| 
|**09/14/15 19:03**|  *amrav*| <@U0AHQ8HD3 amrav> has joined the channel| 
|**09/14/15 20:38**|  *dementor*| d3js real time stats of contribution| 
|**09/14/15 21:10**|  *himanshu*| <@U0AKU18CW himanshu> has joined the channel| 
|**09/14/15 21:53**|  *hargup*| <@U0AJEBGBU hargup> has joined the channel| 
|**09/15/15 08:31**|  *xtinct*| <@U0AHSU2KF xtinct> has joined the channel| 
|**09/15/15 12:16**|  *kumarkrishna*| <@U0AKWDA9H kumarkrishna> has joined the channel| 
|**09/16/15 20:44**|  *twistin*| <@U0AQ1LRBQ twistin> has joined the channel| 
|**09/16/15 23:31**|  *amrav*| New idea proposal: KGP Open Data project. We use embedded devices to relay information to a central server, and this raw data is openly available for anyone to use, for making apps.| 
|**09/16/15 23:34**|  *dementor*| Which data?| 
|**09/16/15 23:34**|  *amrav*| For example, putting embedded devices on buses, that relay current location (wifi module? gps?) and occupancy (ir?). The obvious app application would be a real time map that shows you the buses in real time, along with expected time of arrival, route, etc.| 
|**09/16/15 23:35**|  *amrav*| Another example would be putting embedded devices in restaurants and canteens, that use motion detection to automatically say whether a canteen is open or not, and possibly how crowded it is.| 
|**09/16/15 23:37**|  *amrav*| We also let anyone add new modules to these embedded devices, if they want to add new functionality (provided they dont break the existing stuff)| 
|**09/16/15 23:37**|  *amrav*| <@U0AKR593L>: You have embedded systems experience, right?| 
|**09/16/15 23:38**|  *abhishek*| <@U0AKR593L abhishek> has joined the channel| 
|**09/16/15 23:44**|  *amrav*| <@U0AHQ8HD3 amrav> set the channel purpose: Experimental ideas, useful hacks, and quirky projects, that push the boundaries of how we live and interact in KGP.| 
|**09/17/15 01:25**|  *dementor*| Oooo cool. This will be interesting.| 
|**09/17/15 01:26**|  *dementor*| Crowd detection we can do I think| 
|**09/17/15 01:26**|  *dementor*| Pretty easily| 
|**09/17/15 01:26**|  *dementor*| In Carlos| 
|**09/17/15 01:27**|  *dementor*| Using a pir sensor kept at a strategic place| 
|**09/17/15 02:46**|  *kumarkrishna*| Another form of data could be random tagged images with some Coordinate data embedded in it.| 
|**09/17/15 02:47**|  *kumarkrishna*| It might be easy for people to upload images, taken at random occasions and locations| 
|**09/17/15 02:48**|  *kumarkrishna*| The aim be to try and create a GigaPixel image of KGP| 
|**09/17/15 02:48**|  *kumarkrishna*| (From a particular viewpoint i.e ), we have drones for aerial view as well :stuck_out_tongue:| 
|**09/17/15 23:31**|  *icyflame*| <@U0APA9ZUP icyflame> has joined the channel| 
|**09/18/15 17:55**|  *mitpal*| <@U0AKV0F0W mitpal> has joined the channel| 
|**09/19/15 13:44**|  *hargup*| <@U0AHU8RU0>: <@U0AKGKRST> we were about to meet today to hack on rev-prof search right?| 
|**09/19/15 13:45**|  *dementor*| Yea. I'm fine. Just tell me when.| 
|**09/19/15 13:47**|  *hargup*| lets meet at something around 2:30 at your or nuwanda's room| 
|**09/19/15 13:47**|  *hargup*| btw <@U0AQ1LRBQ> will also join us in| 
|**09/19/15 14:27**|  *nuwanda*| Heyyy guys! Just woke up. Is this happening?| 
|**09/19/15 14:52**|  *dementor*| Yea <@U0AHU8RU0> even I left the bedjust now :stuck_out_tongue:| 
|**09/19/15 20:22**|  *amrav*| Did this happen?| 
|**09/19/15 20:40**|  *dementor*| We met over dinner in mess. Discussed we should order a GPS for now and that we should have a full team meeting to divide work and set milestones.| 
|**09/20/15 13:23**|  *icyflame*| &gt; d3js real time stats of contribution    -- <@U0AKGKRST> (a long time ago :stuck_out_tongue: )    This is pretty easy to implement, but the API is currently not setup for whitelisting origins, it seems.    <@U0AKGKRST> <@U0AHQ8HD3> <@U0AHSU2KF> Can you guys do something about this?    ```  <https://wiki.metakgp.org/api.php?action=query&amp;list=allusers&amp;auprop=editcount&amp;aulimit=50&amp;auwitheditsonly&amp;audir=descending&amp;format=json>  ```  This is the required API endpoint!| 
|**09/20/15 13:27**|  *dementor*| Oh I had thought of this from server end. Client end even I figured there might be issues.| 
|**09/20/15 13:29**|  *icyflame*| Whitelisting seems to be easy. And this resource is not sensitive anyways, so with a sane rate limit, we should not have an issue with exposing this api to everyone.| 
|**09/20/15 13:30**|  *dementor*| <@U0AHQ8HD3> can tell better on this. | 
|**09/20/15 14:11**|  *amrav*| Are you doing authenticated access with a bot? | 
|**09/20/15 14:11**|  *icyflame*| no, I am not| 
|**09/20/15 14:11**|  *icyflame*| But it can be done, if that's all that's stopping me from making the d3.js graph| 
|**09/20/15 14:11**|  *amrav*| If so, I can add your bot to the bots group, which will raise your rate limit. | 
|**09/20/15 14:12**|  *icyflame*| Rate limit is not an issue. Currently, CORS is an issue.| 
|**09/20/15 14:13**|  *amrav*| Ah, I see. What's your origin? | 
|**09/20/15 14:13**|  *icyflame*| ```<http://localhost:8000>``` for now, it would probably change to `<http://icyflame.github.io icyflame.github.io>`, once I host it on GH| 
|**09/20/15 14:14**|  *amrav*| I would recommend getting these stats server side and caching them. We don't want to hit the database everytime somebody loads your page. | 
|**09/20/15 14:17**|  *icyflame*| Do you mean cached on the client side? (I can store a json file and update it at an interval of an hour or something, and render that instead of going hitting the DB everytime someone loads the page.)| 
|**09/20/15 14:17**|  *icyflame*| But what do you mean `cache`? On the server side or the client side?| 
|**09/20/15 14:17**|  *dementor*| That wont be real time :confused:| 
|**09/20/15 14:17**|  *icyflame*| Yeah, that was my concern too.| 
|**09/20/15 14:18**|  *icyflame*| Also, another thing. When someone loads the `Special:ContributorScores` currently, the server does hit the DB right?| 
|**09/20/15 14:19**|  *icyflame*| And you should note that I can load the JSON in the browser (effectively hitting the DB, as many times as I wish) , but not using a AJAX request from `localhost:8000`. I don't understand why that happens either.| 
|**09/20/15 14:20**|  *amrav*| The Special:Contributions page makes a relatively expensive database query to generate those stats. Loading that page once a minute is a non issue. If you load it once a second though, that will probably be heavy on the db (I haven't checked). So if you make a page that uses the api, and that page is loaded several times a minute (say when we release it, or if  we embed it in the main page), then that'll probably be bad. | 
|**09/20/15 14:21**|  *icyflame*| Oh, so, can we generate a JSON file at the server side every minute or two minutes, and I could hit that JSON file instead of hitting the DB?| 
|**09/20/15 14:21**|  *amrav*| For now, I can just enable CORS, and see what happens. If nothing  too bad happens, cool. If not, we'll think about some alternatives. | 
|**09/20/15 14:21**|  *amrav*| Yeah, that's what I was thinking. | 
|**09/20/15 14:23**|  *icyflame*| Okay, that sounds good. :+1:| 
|**09/20/15 15:33**|  *amrav*| <@U0APA9ZUP>: Ive enabled CORS from any origin. See <https://www.mediawiki.org/wiki/API:Cross-site_requests>, in particular, you need to pass `origin` even as a query parameter.| 
|**09/20/15 15:33**|  *icyflame*| Yeah, i have already seen that doc. Thanks a lot! :simple_smile:| 
|**09/21/15 00:29**|  *icyflame*| <!channel>: Contribution graph works! :smile:     <http://icyflame.github.io/metakgp-visualize/>| 
|**09/21/15 00:29**|  *dementor*| I dont like this :confused:| 
|**09/21/15 00:31**|  *dementor*| There should be a filter of last week and stuff too else I feel so low :confused:| 
|**09/21/15 00:31**|  *dementor*| <@U0AHQ8HD3>: This should be there on the Main Page too :smile:| 
|**09/21/15 00:33**|  *amrav*| <@U0APA9ZUP>: Wow, thats really pretty. I bet you can give it some real bells and whistles though - how about custom date ranges, that make the graph animate and change? :simple_smile:| 
|**09/21/15 00:33**|  *icyflame*| Yeah, I was thinking about that too| 
|**09/21/15 00:33**|  *icyflame*| any ideas as to what can be done? perhaps one page's contributions?| 
|**09/21/15 00:33**|  *amrav*| If you can make this stable enough, it could be a really popular mediawiki extension.| 
|**09/21/15 00:34**|  *amrav*| Also, number of contributions may not be as important as size (and discounting moves and renames)| 
|**09/21/15 00:34**|  *dementor*| Also, what score are you plotting?   &lt;Acting like a muggu for marks&gt;| 
|**09/21/15 00:35**|  *dementor*| ^Exactly| 
|**09/21/15 00:35**|  *icyflame*| It's the editcount :stuck_out_tongue:| 
|**09/21/15 00:35**|  *icyflame*| the total number of edits, I believe. I am not sure how the contribution scores are calculated. But plotting them should be a trivial issue, once I know how they are calculated.| 
|**09/21/15 00:36**|  *amrav*| MediaWiki uses a score to rank users, which is some function of editcount and edit size.| 
|**09/21/15 00:36**|  *dementor*| ```The score primarily measures unique pages edited, with consideration for high edit volume.```| 
|**09/21/15 00:37**|  *icyflame*| The API does not support an endpoint that returns score, so we may have to calculate it ourself.| 
|**09/21/15 00:37**|  *amrav*| You can write the function youre using to calculate score in MathTex on the page. Make it look really fancy :stuck_out_tongue:| 
|**09/21/15 00:37**|  *amrav*| Yeah, that score is not a public thing. Which is fine, you can come up with your own function, and keep tweaking it as you understand more about whats important.| 
|**09/21/15 00:38**|  *amrav*| (or you can look at mw source to see how theyre doing it)| 
|**09/21/15 00:38**|  *dementor*| <https://www.mediawiki.org/wiki/Extension:Contribution_Scores>| 
|**09/21/15 00:38**|  *dementor*| No it is :stuck_out_tongue:| 
|**09/21/15 00:38**|  *dementor*| ```The score is defined as (number of unique pages edited) + 2 * square root ((number of edits) - (number of unique pages edited)).```| 
|**09/21/15 00:43**|  *himanshu*| This function for score seems better than plain edit count| 
|**09/21/15 00:43**|  *himanshu*| Very nice work <@U0APA9ZUP> :simple_smile:| 
|**09/21/15 00:45**|  *dementor*| <!channel>:  We can have an extension of imdb for Kgp, Adding reviews for plays and actors. We have hell lot of plays around the year.| 
|**09/21/15 00:45**|  *dementor*| There is someone from a different time zone here? :open_mouth: Bots?| 
|**09/21/15 00:47**|  *icyflame*| no <@U0AKWDA9H> has set himself to UTC-2 :stuck_out_tongue:| 
|**09/21/15 00:48**|  *dementor*| UTC -2  :O| 
|**09/21/15 00:48**|  *dementor*| Thats like only Greenland I think| 
|**09/21/15 00:58**|  *icyflame*| <@U0APA9ZUP icyflame> pinned a message to this channel.| 
