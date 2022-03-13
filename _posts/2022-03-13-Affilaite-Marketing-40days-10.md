---
layout: post
title:  "第10天，在PropellerAds设置Campaign"
categories: [ affiliate ]
image: assets/images/4.jpg
typora-root-url: ..
excerpt: 这个教程主要讲怎么在流量源上设置Campaign，使用的示例是PropellerAds。
---
上个教程实际操作和解释了怎么在Voluum上设置campaign，这个教程主要讲怎么在流量源上设置Campaign，使用的示例是PropellerAds。

##### 实际操作

PropellerAds申请通过后充值个最低金额100刀即可，充值的地方在PropellerAds的控制面板“Add Funds”那里，提供了挺多的充值方式，其中包含了支付宝，国人可能更喜欢这种方式，这里不得不吐槽一下，充值的手续费巨贵贵，100刀要收2.64刀，每每充值都是肉疼。

充值好了之后就可以按照下面的步骤创建Campaign:

1、登陆进入PropellerAds，在左侧的菜单中点击“Campaigns”,点击“Create Campaign”按钮。

2、Campaign的名字保持和Voluum中的campaign的名字一致。

3、“Choosse Advertising Format”是广告形式，这里选择“Onclick(Popunder)”。

4、“Pricing Model”是出价方式，这里选择“SmartCPM”,这是实时竞价模式。

5、“Target URL”就是要推广的广告链接，复制在Voluum中创建的campaign的推广链接，链接在Voluum中的位置如下图所示

![img](/assets/images/2022-03-13-Affilaite-Marketing-40days-10/voluum-1.png)

6、“Frequency/Capping”设置为“enabled”，设置广告展示的频率为“One visitor will see your ad **1** times per **24** hours”。

7、“Traffic Options”选择“All Traffic“，去掉”Include Broker Traffic“和”Allow Anti-Adblock Traffic“的勾选。

8、”Automatic optimization“保持默认的”disabled“，”Traget CPA“同样的操作。

9、”Countries“选择Offer所在的默认的国家，CPM是出价，这里先设置为1，后面会将怎么确定设置出价。”Cities“保持默认

10、设置”Daily Campaign Budget“和”Total Campaign Budget“为10$，这是最低的预算。

11、保持”Audience“为默认，实际上就是nothing selected.

12、”Campaign Schedule“设置：

> a、”Select Timezone“保持默认即可，这是设置的时区，下面的时间列表是设置广告在哪些时间段运行，现在保持全天运行。
>
> b、”Ad delivery method“是设置预算怎么花，这里选择”Standard“。

13、”Targeting“是设置目标人群。

> a、”Platform“是设置平台的，这里选择”Mobile“
>
> b、”OS“是设置操作系统的，如果你的offer需要特殊的操作系统，可以在这里选择，有五个选项，如下图所示：
>
> ![img](/assets/images/2022-03-13-Affilaite-Marketing-40days-10/os.png)
>
> 需要注意Windows Mobile和Windows Phone指的是同一种操作系统，RIM和Blackberry也是一样的，在Offer中可能会有不同的描述。
>
> c、”Browser“是选择浏览器的，”include“是包含后面选择的浏览器。
>
> d、”Browser language“是选择流量器语言，按需设置。
>
> e、”Connection type“是网络类型，如果你的offer是1-click或者2-click类型的offer请选择”3G/LTE“,这些offer只接受移动流量，不支持”wifi“。
>
> f、”Mobile ISP“是移动流量的运营商，只有选择了”3G/LTE“之后才能设置，按需设置即可。
>
> g、”Zone limitation“现在留空。

14、勾选”I declare and guarantee that my campaign meets the Quality Guidelines“并点击”Start Campaign“

Campaign设置好之后不会立刻得到流量，PropellerAds会对你的广告进行审核，审核不通过会打回来让你修改，现在PropellerAds的政策还是比较严格的，按照它们的要求修改广告文案，重新提交几次就会知道他们的底线了。
