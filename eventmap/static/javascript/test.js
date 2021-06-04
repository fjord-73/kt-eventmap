
window.onload = function() {
  
  var f = document.getElementById('popup');
  ff = f.textContent.substr(13)
  
  
  if(ff.match("東京都")){
    document.getElementById('tokyo').style.backgroundColor= '#2196F3';
  }
  if(ff.match("神奈川県")){
    document.getElementById('kanagawa').style.backgroundColor= '#2196F3';
  }
  if(ff.match("埼玉県")){
    document.getElementById('saitama').style.backgroundColor= '#2196F3';
  }
  if(ff.match("千葉県")){
    document.getElementById('chiba').style.backgroundColor= '#2196F3';
  }
  if(ff.match("茨城県")){
    document.getElementById('ibaraki').style.backgroundColor= '#2196F3';
  }
  if(ff.match("栃木県")){
    document.getElementById('tochigi').style.backgroundColor= '#2196F3';
  }
  if(ff.match("群馬県")){
    document.getElementById('gunnma').style.backgroundColor= '#2196F3';
  }
  if(ff.match("北海道")){
    document.getElementById('hokkaido').style.backgroundColor= '#673AB7';
  }
  if(ff.match("青森県")){
    document.getElementById('aomori').style.backgroundColor= '#3F51B5';
  }
  if(ff.match("秋田県")){
    document.getElementById('akita').style.backgroundColor= '#3F51B5';
  }
  if(ff.match("岩手県")){
    document.getElementById('iwate').style.backgroundColor= '#3F51B5';
  }
  if(ff.match("山形県")){
    document.getElementById('yamagata').style.backgroundColor= '#3F51B5';
  }
  if(ff.match("宮城県")){
    document.getElementById('miyagi').style.backgroundColor= '#3F51B5';
  }
  if(ff.match("石川県")){
    document.getElementById('isikawa').style.backgroundColor= '#009688';
  }
  if(ff.match("富山県")){
    document.getElementById('toyama').style.backgroundColor= '#009688';
  }
  if(ff.match("新潟県")){
    document.getElementById('niigata').style.backgroundColor= '#009688';
  }
  if(ff.match("福島県")){
    document.getElementById('hukusima').style.backgroundColor= '#3F51B5';
  }
  if(ff.match("福井県")){
    document.getElementById('hukui').style.backgroundColor= '#009688';
  }
  if(ff.match("岐阜県")){
    document.getElementById('gihu').style.backgroundColor= '#009688';
  }
  if(ff.match("長野県")){
    document.getElementById('nagano').style.backgroundColor= '#009688';
  }
  if(ff.match("佐賀県")){
    document.getElementById('saga').style.backgroundColor= '#f44336';
  }
  if(ff.match("福岡県")){
    document.getElementById('hukuoka').style.backgroundColor= '#f44336';
  }
  if(ff.match("大分県")){
    document.getElementById('ooita').style.backgroundColor= '#f44336';
  }
  if(ff.match("山口県")){
    document.getElementById('yamaguti').style.backgroundColor= '#FF9800';
  }
  if(ff.match("島根県")){
    document.getElementById('simane').style.backgroundColor= '#FF9800';
  }
  if(ff.match("兵庫県")){
    document.getElementById('hyougo').style.backgroundColor= '#FFC107';
  }
  if(ff.match("京都府")){
    document.getElementById('kyoto').style.backgroundColor= '#FFC107';
  }
  if(ff.match("滋賀県")){
    document.getElementById('siga').style.backgroundColor= '#FFC107';
  }
  if(ff.match("長崎県")){
    document.getElementById('nagasaki').style.backgroundColor= '#f44336';
  }
  if(ff.match("熊本県")){
    document.getElementById('kumamoto').style.backgroundColor= '#f44336';
  }
  if(ff.match("宮崎県")){
    document.getElementById('miyazaki').style.backgroundColor= '#f44336';
  }
  if(ff.match("広島県")){
    document.getElementById('hirosima').style.backgroundColor= '#FF9800';
  }
  if(ff.match("岡山県")){
    document.getElementById('okayama').style.backgroundColor= '#FF9800';
  }
  if(ff.match("大阪府")){
    document.getElementById('oosaka').style.backgroundColor= '#FFC107';
  }
  if(ff.match("奈良県")){
    document.getElementById('nara').style.backgroundColor= '#FFC107';
  }
  if(ff.match("三重県")){
    document.getElementById('mie').style.backgroundColor= '#FFC107';
  }
  if(ff.match("愛知県")){
    document.getElementById('aichi').style.backgroundColor= '#009688';
  }
  if(ff.match("山梨県")){
    document.getElementById('yamanasi').style.backgroundColor= '#009688';
  }
  if(ff.match("愛媛県")){
    document.getElementById('ehime').style.backgroundColor= '#FF5722';
  }
  if(ff.match("香川県")){
    document.getElementById('kagawa').style.backgroundColor= '#FF5722';
  }
  if(ff.match("和歌山県")){
    document.getElementById('wakayama').style.backgroundColor= '#FFC107';
  }
  if(ff.match("静岡県")){
    document.getElementById('shizuoka').style.backgroundColor= '#009688';
  }
  if(ff.match("鹿児島県")){
    document.getElementById('kagosima').style.backgroundColor= '#f44336';
  }
  if(ff.match("高知県")){
    document.getElementById('kouchi').style.backgroundColor= '#FF5722';
  }
  if(ff.match("徳島県")){
    document.getElementById('tokusima').style.backgroundColor= '#FF5722';
  }
  if(ff.match("沖縄県")){
    document.getElementById('okinawa').style.backgroundColor= '#E91E63';
  }
}
var scrollAnimationElm = document.querySelectorAll('.sa');
var scrollAnimationFunc = function() {
  for(var i = 0; i < scrollAnimationElm.length; i++) {
    var triggerMargin = 300;
    if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
      scrollAnimationElm[i].classList.add('show');
    }
  }
}
window.addEventListener('load', scrollAnimationFunc);
window.addEventListener('scroll', scrollAnimationFunc);
