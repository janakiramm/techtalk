function main(params) {
    return new Promise(function(resolve, reject) {
        if (!params.from || !params.to || !params.subject || !params.content) {
            reject("Insufficient number of parameters");
        }
        var helper = require('sendgrid').mail
        var sg = require('sendgrid')("<SENDGRID_API_KEY");

        from_email = new helper.Email(params.from)
        to_email = new helper.Email(params.to)
        subject = params.subject
        content = new helper.Content("text/plain", params.content)
        mail = new helper.Mail(from_email, subject, to_email, content)

        var request = sg.emptyRequest({
            method: 'POST',
            path: '/v3/mail/send',
            body: mail.toJSON()
        });

        sg.API(request, function(error, response) {
            if (error) {
                reject(error);
            } else {
                console.log(response.statusCode)
                console.log(response.body)
                console.log(response.headers)
                resolve({
                    msg: "Message sent!"
                });
            }
        })
    });
}
exports.main = main;