/*
hello v1.0.0

重写: 打开支付宝-hello小程序
[task_local]
#hello
57 0,9 * * * https://raw.githubusercontent.com/Origin-wu/Test/main/hello.js, tag=hello, enabled=true
[rewrite_local]
mtop.alsc url script-request-header https://raw.githubusercontent.com/Origin-wu/Test/main/hello.js
[MITM]
hostname = *

cron: 57 0,9 * * *
const $ = new Env("hello");
*/


int main(void)
{
    return 1;
}
