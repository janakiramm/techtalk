function main(params) {
    return new Promise(function(resolve, reject) {
        if (!params.order || !params.manager) {
            reject("Insufficient number of parameters");
        }

        if (params.order < 10000) {
            console.log(message);
            resolve({
                order: "Low value order"
              });
            return;
        }

        var helper = require('sendgrid').mail
        var sg = require('sendgrid')("<SENDGRID_API_KEY>");

        from_email = new helper.Email("<FROM_EMAIL>")
        to_email = new helper.Email("<TO_EMAIL>")
        subject = "High Value Order Alert"
        message = 'High value order worth $' + params.order + ' is closed by ' + params.manager;
        content = new helper.Content("text/plain", message)
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