---
layout: post
title:  "第9天，在Voluum上设置数据追踪"
categories: [ affiliate ]
image: assets/images/2.jpg
typora-root-url: ..
excerpt: 追踪系统是收集数据的重要工具，Vortex的这篇教程详细描述了怎么在Voluum上设置数据追踪。
---
追踪系统是收集数据的重要工具，Vortex的这篇教程详细描述了怎么在Voluum上设置数据追踪。

我使用过RedTracker,Bemob和adsBride，这些都是部署在云端的追踪系统，主要功能上都是相同的，但是每一个都有自己的特色，最终我选择了Bemob。

[Bemob](https://bemob.com/)的功能在这几个里面不算是最强，但UI是最舒服的，而且对新人友好，有免费使用额度。

[![img](/assets/images/2022-03-13-Affilaite-Marketing-40days-9/download-2.png)](https://bemob.com/?ref=eg53ohfxhu)

##### 实际操作

##### **1、设置流量源**

在Voluum的操作路径是“Traffic sources”>”New traffic source”>”Trusted Traffic Source Templates”>“PropellerAds”,点击“Load template”然后点击“Save”.

##### **2、设置广告联盟**

在Voluum的操作路径是“Affiliate networds”>”+ New affiliate netword”>在“Affiliate network name”字段中用“Mobidea”过滤，选择“Mobidea”后点击保存。

##### **3、设置广告联盟的转化回调链接**

先在Voluum中到设置页面，”Domains“选项卡中，复制”Main Domain“

然后登录到Mobidea，点击右上角的小齿轮，进行全局回调链接的设置，点击“Vlobal postback”，选择”Voluum”，把上一步复制的Main Domain填到这里。

这里Mobidea帮我们做了很多事情，回调参数自动帮我们填写了，如果是未列在里面的追踪系统就要自己设置Token了。

![img](/assets/images/2022-03-13-Affilaite-Marketing-40days-9/屏幕截图-2020-10-31-161451.png)

滚动到下面，点击保存，广告联盟的转化回调链接就设置完成了。

##### **4、在Voluum中创建Offer**

复制下来offer的推广链接，应该是下面的样子：

```
https://www.rotatemyurls.com/offer/11111|13456?data1=Track1&data2=Track2&tag={Externa l_ID_from_traffic_source}&website={subID}&placemen t={sub_subID}
```

把里面需要传给广告联盟的参数替换为Tracker的占位符，最后得到的链接如下：

```
https://www.rotatemyurls.com/offer/11111|13456?tag={clickid}&website={trafficsource.id}&placement={campaign.id}
```

有很多追踪系统连这后面的占位替换也会帮我们完成，比如Bemob，这时候创建Offer的时候填进去的链接仅仅是下面的样子：

```
https://www.rotatemyurls.com/offer/11111|13456?data1=Track1&data2=Track2
```

Volumm中创建Offer的路径是”Offers“>”+ New Offer”. 粘贴上面的链接到Url中。

“Affliate Network”选择”Mobidea”。

”Country Tag“选择Offer的目标国家。

点击”Save“，Offer就创建完毕。

##### **5、在Voluum中创建Campaign**

campaign是营销活动，把我们的流量源，offer，Lander融合在一起构建。

在Voluum中创建campaign的路径是：”Campaigns“>”+ New campaing”.

Campaign的命名也是一门学问，创建10-20个Campaign后如果你还能一眼识别出来他们都是做什么的，这样命名是比较好的，最终每个人都会形成自己的命名习惯，现在可以按照这个模板命名

**[日期] [国家简称]Main[网络类型] [任何其他你想要的标识]**

[日期]中可以填如你开始campaign的时间，可以有任何你喜欢的格式。

Main的含义是主流的，就是没有成人内容。

[Carrieer]就是流量的网络运营商，在之后的教程里会有讲解，如果一个offer可以在多个网络运营商上跑，现在选一个就可以了。

现在我要在ZA的Vodacom上推广Gameloft，campaign名字就可以命名如下

> **110218 ZA Main Vodacom Gameloft**

设置”Country tag“为你选中的国家

”Traffic source“选择”Propeller Ads“

”Cost Model“选择”Auto“，因为我们是动态竞价的，所以流量平台会把每一次的出价都传给我们。

点击”Next“到”DESTINATION“页面，选择”Path“，”Path name“填如”1“。

勾选”Direct linking“，点击数据字段”1. Select offer“，然后选择我们要推广的offer。

然后点击保存，这时候”Campaign URL“就会出现了，现在先忽略它，下一节可能将会讲解怎么用这个链接在PropellerAds上创建campaign。

至此，在Voluum上创建campaign的工作都做完了。

##### 操作解释

首先出现在你脑海中的一个疑问一定是：我们为什么需要一个Tracker？Tracker的主要用途列举如下。

**1、检测访问者的详细信息，统计和展示这些数据。**

Voluum可以检测访问者的详细信息，比如IP地址，国家，操作系统，设备品牌，联网类型3G或者Wifi，浏览器等等，这会有助于我们优化campaign，比如有些操作系统让我们损失严重，其他的操作系统给我带来利润，我们就可以拉黑这个操作系统。

**2、控制流量的流向**

当你在Voluum中创建了campaign后，你就会很清楚地知道如何把访问者送到什么地方，比如你可以把他们直接带到Offer页面，或者带到landing page页面，也被称为lander,preLander,presell page或者bridge page,先对用户进行一个预售，当他们点击行动按钮，说明他们对offer感兴趣，就会增加他们转化offer的概率。

如果没有访问者的转化信息，你就会跟瞎子一样，很难去优化campaign。
