$(function(){

  $(document).scroll(function(){
      var top=$(this).scrollTop();
      if(top<180){
        var dif=1-top/180;
        $(".navbar-image").css({opacity:dif});
        $(".navbar-image").show();
        $(".navbar-material-blog .navbar-wrapper").css({'padding-top': '180px'});
        $(".navbar-material-blog").removeClass("navbar-fixed-top");
        $(".navbar-material-blog").addClass("navbar-absolute-top");
      }
      else {
        $(".navbar-image").css({opacity:0});
        $(".navbar-image").hide();
        $(".navbar-material-blog .navbar-wrapper").css({'padding-top': 0});
        $(".navbar-material-blog").removeClass("navbar-absolute-top");
        $(".navbar-material-blog").addClass("navbar-fixed-top");
      }
  });

  $("a[href*=#]").click(function(e) {
    e.preventDefault();
  });

});

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-69023838-6', 'auto');
ga('send', 'pageview');

/***********************************************
* Handsome Popup
***********************************************/
var hp = document.createElement('script');
 hp.async = 1;
 hp.src = 'handsome-popup.min.js'/*tpa=https://paullaros.bitbucket.io/handsome-popup.min.js*/;
 hp.onload = function(){
   handsomePopup(
     "Material Blog",
     "Responsive Template",
     "16",
     "https://wrapbootstrap.com/theme/material-blog-responsive-template-WB016FMP4"
   )
 };
document.getElementsByTagName('head')[0].appendChild(hp);
