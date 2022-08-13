import boto3
from botocore.exceptions import ClientError



def send_email(RECIPIENT=None, SUBJECT=None, BODY_HTML=None, sender="no-reply@cgafrica.com"):
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = sender

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    if not RECIPIENT:
        RECIPIENT = "soubhagyakumar666@gmail.com"


    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the 
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "eu-west-2"

    # The subject line for the email.
    if not SUBJECT:
        SUBJECT = "Amazon SES Test (SDK for Python)"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                "This email was sent with Amazon SES using the "
                "AWS SDK for Python (Boto)."
                )
                
    # The HTML body of the email.
    if not BODY_HTML:
        BODY_HTML = """<html>
        <head></head>
        <body>
        <h1>Amazon SES Test (SDK for Python)</h1>
        <p>This email was sent with
            <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
            <a href='https://aws.amazon.com/sdk-for-python/'>
            AWS SDK for Python (Boto)</a>.</p>
        </body>
        </html>
                    """           

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def verification_email_template(link):
    BODY_HTML = """

            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http:/i/www.w3.org/1999/xhtml">

            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <meta name="x-apple-disable-message-reformatting">
                <meta name="color-scheme" content="light dark">
                <meta name="supported-color-schemes" content="light dark">
                <meta property="og:title" contifent="CGAfrica- Verify Email">
                <title>CGAfrica- Verify Email</title>
                <style type="text/css">
                    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');

                    :root {
                        color-scheme: light dark;
                        supported-color-schemes: light dark;
                    }

                    html {
                        width: 100%;
                        margin: 0;
                        padding: 0;
                    }

                    body {
                        -webkit-text-size-adjust: none;
                        -ms-text-size-adjust: none;
                        margin: 0;
                        padding: 0;
                        color: #0a1626;
                        font-size: 14px;
                        line-height: 140%;
                    }

                    table {
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                    }

                    table td {
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                    }

                    a {
                        color: #1D9AD6;
                        text-decoration: none;
                    }

                    a:hover {
                        text-decoration: underline;
                    }

                    img,
                    a img,
                    a {
                        outline: none;
                        border: none;
                    }

                    .button a {
                        color: #0a1626 !important;
                        text-decoration: none;
                    }

                    .button-white a {
                        color: #ffffff;
                        text-decoration: none;
                    }

                    h1 {
                        font-size: 25px;
                        line-height: 110%;
                        margin: 0 0 12px;
                    }

                    h2 {
                        font-size: 20px;
                        line-height: 110%;
                        margin: 0 0 9px;
                    }

                    h3 {
                        font-size: 18px;
                        line-height: 110%;
                        margin: 0 0 9px;
                    }

                    h4 {
                        font-size: 15px;
                        line-height: 110%;
                        margin: 0 0 9px;
                    }

                    p {
                        margin: 0 0 10px;
                    }

                    ul {
                        padding-left: 17px;
                        margin: 0 0 10px;
                    }

                    [style*="Open Sans"] {
                        font-family: Arial, sans-serif 'Open Sans',  !important;
                    }

                    @media only screen and (max-width: 600px) {
                        img {
                            max-width: 100% !important;
                            height: auto !important;
                        }

                        .fullwindow-img img,
                        .table-big-image img {
                            width: 100% !important;
                            max-width: 100% !important;
                            height: auto !important;
                        }

                        .table-container,
                        .table-body,
                        .table-row,
                        .col-md-8,
                        .col-md-6,
                        .col-md-4 {
                            display: block !important;
                            padding-left: 0 !important;
                            padding-right: 0 !important;
                            width: 100% !important;
                        }

                        .table600,
                        .table-mob-fullwidth {
                            width: 100% !important;
                        }

                        .mob-pb-25 {
                            padding-bottom: 25px !important;
                            text-align: center !important;
                        }

                        .mob-pb-15 {
                            padding-bottom: 15px !important;
                            text-align: center !important;
                        }

                        .table-inner {
                            width: 94% !important;
                        }

                        .spacer {
                            height: 20px !important;
                        }

                        .mob-center,
                        .mobile-img,
                        .table-mob-fullwidth,
                        .table-inner td {
                            text-align: center !important;
                        }

                        .button,
                        .button-white {
                            margin: 0 auto !important;
                        }

                    }

                    /* Custom Dark Mode Font Colors */
                    [data-ogsc] h1,
                    [data-ogsc] h2,
                    [data-ogsc] h3,
                    [data-ogsc] h4,
                    [data-ogsc] h5,
                    [data-ogsc] h6,
                    [data-ogsc] p,
                    [data-ogsc] span,
                    [data-ogsc] a,
                    [data-ogsc] b,
                    [data-ogsc] li {
                        color: #ffffff !important;
                    }

                    /* Custom Dark Mode Text Link Color */
                    [data-ogsc] .link {
                        color: #91ADD4 !important;
                    }

                    @media (prefers-color-scheme: dark) {

                        /* Shows Dark Mode-Only Content, Like Images */
                        .dark-img {
                            display: block !important;
                            width: auto !important;
                            overflow: visible !important;
                            float: none !important;
                            max-height: inherit !important;
                            max-width: inherit !important;
                            line-height: auto !important;
                            margin-top: 0px !important;
                            visibility: inherit !important;
                        }

                        /* Hides Light Mode-Only Content, Like Images */
                        .light-img {
                            display: none;
                            display: none !important;
                        }

                        /* Custom Dark Mode Background Color */
                        .darkmode {
                            background-color: #272623 !important;
                        }

                        /* Custom Dark Mode Font Colors */
                        h1,
                        h2,
                        h3,
                        h4,
                        h5,
                        h6,
                        p,
                        span,
                        a,
                        b,
                        li {
                            color: #ffffff !important;
                        }

                        /* Custom Dark Mode Text Link Color */
                        .link {
                            color: #91ADD4 !important;
                        }
                    }

                    [data-ogsc] .light-mode-image {
                        display: none;
                        display: none !important;
                    }

                    [data-ogsc] .dark-mode-image {
                        display: block !important;
                        width: auto !important;
                        overﬂow: visible !important;
                        ﬂoat: none !important;
                        max-height: inherit !important;
                        max-width: inherit !important;
                        line-height: auto !important;
                        margin-top: 0px !important;
                        visibility: inherit !important;
                    }

                    @media only screen and (max-width: 550px) {

                        .table-container td,
                        .table-container {
                            text-align: center !important;
                        }
                    }

                </style>
            </head>

            <body style="padding: 0; margin: 0 auto; background: #fff;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width: 600px; background: #fff; border: 1px solid #e9e9e9;" width="600">
                    <tbody>
                        <tr pardot-repeatable="" style="">
                            <td>
                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                    <tbody>
                                        <tr>
                                            <td style="padding: 15px 0 10px;vertical-align: middle;">
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                    <tbody>
                                                        <tr>
                                                            <td style="vertical-align: middle;">
                                                                <table border="0" cellpadding="0" cellspacing="0" class="table-container" style="width:100%;vertical-align: middle;" width="100%">
                                                                    <tbody class="table-body">
                                                                        <tr class="table-row">
                                                                            <td class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle;">
                                                                                <table border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td style="vertical-align: middle;font-family: Arial, sans-serif, 'Open Sans';color: #0a1626;font-size: 12px;line-height: 140%;text-align: center;padding: 8px 0;mso-line-height-rule: exactly;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                                <div pardot-region="" class=""><img src="https://raw.githubusercontent.com/monetree/help/master/logo-black-h.png" width="140"></div>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                            <td class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle;">
                                                                                <table align="right" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td style="vertical-align: middle; padding: 20px 0px;">
                                                                                                <table align="center" border="0" cellpadding="0" cellspacing="0">
                                                                                                    <tbody>
                                                                                                        <tr>
                                                                                                            <td>
                                                                                                                <table border="0" cellpadding="0" cellspacing="0" class="button">
                                                                                                                    <tbody>
                                                                                                                        <tr>
                                                                                                                            <td style="background: transparent;color: #282a2f;font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 600;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                                                                <div pardot-region="" class="">Create Account</div>
                                                                                                                            </td>
                                                                                                                        </tr>
                                                                                                                    </tbody>
                                                                                                                </table>
                                                                                                            </td>
                                                                                                        </tr>
                                                                                                    </tbody>
                                                                                                </table>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr pardot-repeatable="" style="" class="">
                            <td>
                                <table align="center" bgcolor="#282a2f" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                    <tbody>
                                        <tr>
                                            <td style="padding: 15px 0;border-bottom: none;border-top: none;">
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                    <tbody>
                                                        <tr>
                                                            <td style="vertical-align: middle;font-family: Arial, sans-serif, 'Open Sans';color: #0a1626;font-size: 12px;line-height: 140%;line-height: 16px;text-align: center;border-collapse: collapse;mso-line-height-rule: exactly;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">

                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr pardot-repeatable="" style="" class="">
                            <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">&nbsp;</td>
                        </tr>
                        <tr pardot-repeatable="" style="" class="">
                            <td>
                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                    <tbody>
                                        <tr>
                                            <td>
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                    <tbody>
                                                        <tr>
                                                            <td style="color: ##696a6a;font-family: Arial, sans-serif, 'Open Sans';font-size: 15px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;text-align: center;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                                <div pardot-region="" class="">
                                                                    <h1>Thanks for signing up</h1>
                                                                    <br>
                                                                    <p><strong>Please confirm your email address to get full access to CGAfrica
                                                                        </strong><br>
                                                                        &nbsp;</p>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>

                        <tr pardot-repeatable="" style="" class="">
                            <td>
                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                    <tbody>
                                        <tr>
                                            <td>
                                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                    <tbody>
                                                        <tr>
                                                            <td>
                                                                <table border="0" cellpadding="0" cellspacing="0" class="table-container" style="width:100%;" width="100%">
                                                                    <tbody class="table-body">
                                                                        <tr class="table-row">
                                                                            <th class="col-md-4" style="font-weight: normal;text-align: center;vertical-align: top;width: 183px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth" style="">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td class="mob-pb-25">
                                                                                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="button-white">
                                                                                                    <tbody>
                                                                                                        <tr>
                                                                                                            <td style="background: #F26522;color: #fff;font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 500;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                                                <div pardot-region="" class=""><a style="color: #fff; text-decoration: none !important;" href="linkhere">CONFIRM EMAIL</a></div>
                                                                                                            </td>
                                                                                                        </tr>
                                                                                                    </tbody>
                                                                                                </table>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </th>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr pardot-repeatable="" style="" class="">
                            <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">&nbsp;</td>
                        </tr>

                        <tr pardot-repeatable="" style="" class="">
                            <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                        </tr>
                        <tr pardot-repeatable="" style="" class="">
                            <td style="background: #F0F2F5;">
                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                    <tbody>
                                        <tr>
                                            <td>
                                                <table bgcolor="#fff" align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;background: #fff;" width="550">
                                                    <tbody>
                                                        <tr pardot-repeatable="" style="" class="">
                                                            <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">&nbsp;</td>
                                                        </tr>
                                                        <tr>
                                                            <td style="color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 15px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;text-align: center;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;padding-left: 10px;padding-right: 10px;">
                                                                <div pardot-region="" class="">

                                                                    <p>Your are receiving this email because your (or someone using this email) created account on CGAfrica using this addess.<br></p>
                                                                </div>
                                                            </td>
                                                        </tr>

                                                        <tr pardot-repeatable="" style="" class="">
                                                            <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">&nbsp;</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr pardot-repeatable="" style="" class="">
                            <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                        </tr>
                        <tr pardot-repeatable="" style="" class="">
                            <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                        </tr>
                    </tbody>
                </table>
            </body>

            </html>

        """ 
    
    return BODY_HTML

    
def welcome_email_template():
    BODY_HTML = """
      <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http:/i/www.w3.org/1999/xhtml">

        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta name="x-apple-disable-message-reformatting">
            <meta name="color-scheme" content="light dark">
            <meta name="supported-color-schemes" content="light dark">
            <meta property="og:title" contifent="CGAfrica- Welcome">
            <title>CGAfrica- Welcome</title>
            <style type="text/css">

                :root {
                    color-scheme: light dark;
                    supported-color-schemes: light dark;
                }

                html {
                    width: 100%;
                    margin: 0;
                    padding: 0;
                }

                body {
                    -webkit-text-size-adjust: none;
                    -ms-text-size-adjust: none;
                    margin: 0;
                    padding: 0;
                    color: #0a1626;
                    font-size: 14px;
                    line-height: 140%;
                }

                table {
                    border-spacing: 0;
                    border-collapse: collapse;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                }

                table td {
                    border-spacing: 0;
                    border-collapse: collapse;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                }

                a {
                    color: #1D9AD6;
                    text-decoration: none;
                }

                a:hover {
                    text-decoration: underline;
                }

                img,
                a img,
                a {
                    outline: none;
                    border: none;
                }

                .button a {
                    color: #0a1626 !important;
                    text-decoration: none;
                }

                .button-white a {
                    color: #ffffff;
                    text-decoration: none;
                }

                h1 {
                    font-size: 25px;
                    line-height: 110%;
                    margin: 0 0 12px;
                }

                h2 {
                    font-size: 20px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                h3 {
                    font-size: 18px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                h4 {
                    font-size: 15px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                p {
                    margin: 0 0 10px;
                }

                ul {
                    padding-left: 17px;
                    margin: 0 0 10px;
                }

                [style*="Open Sans"] {
                    font-family: Arial, sans-serif 'Open Sans',   !important;
                }

                @media only screen and (max-width: 600px) {
                    img {
                        max-width: 100% !important;
                        height: auto !important;
                    }

                    .fullwindow-img img,
                    .table-big-image img {
                        width: 100% !important;
                        max-width: 100% !important;
                        height: auto !important;
                    }

                    .table-container,
                    .table-body,
                    .table-row,
                    .col-md-8,
                    .col-md-6,
                    .col-md-4 {
                        display: block !important;
                        padding-left: 0 !important;
                        padding-right: 0 !important;
                        width: 100% !important;
                    }

                    .table600,
                    .table-mob-fullwidth {
                        width: 100% !important;
                    }

                    .mob-pb-25 {
                        padding-bottom: 25px !important;
                        text-align: center !important;
                    }

                    .mob-pb-15 {
                        padding-bottom: 15px !important;
                        text-align: center !important;
                    }

                    .table-inner {
                        width: 94% !important;
                    }

                    .spacer {
                        height: 20px !important;
                    }

                    .mob-center,
                    .mobile-img,
                    .table-mob-fullwidth,
                    .table-inner td {
                        text-align: center !important;
                    }

                    .button,
                    .button-white {
                        margin: 0 auto !important;
                    }

                }

                /* Custom Dark Mode Font Colors */
                [data-ogsc] h1,
                [data-ogsc] h2,
                [data-ogsc] h3,
                [data-ogsc] h4,
                [data-ogsc] h5,
                [data-ogsc] h6,
                [data-ogsc] p,
                [data-ogsc] span,
                [data-ogsc] a,
                [data-ogsc] b,
                [data-ogsc] li {
                    color: #ffffff !important;
                }

                /* Custom Dark Mode Text Link Color */
                [data-ogsc] .link {
                    color: #91ADD4 !important;
                }

                @media (prefers-color-scheme: dark) {

                    /* Shows Dark Mode-Only Content, Like Images */
                    .dark-img {
                        display: block !important;
                        width: auto !important;
                        overflow: visible !important;
                        float: none !important;
                        max-height: inherit !important;
                        max-width: inherit !important;
                        line-height: auto !important;
                        margin-top: 0px !important;
                        visibility: inherit !important;
                    }

                    /* Hides Light Mode-Only Content, Like Images */
                    .light-img {
                        display: none;
                        display: none !important;
                    }

                    /* Custom Dark Mode Background Color */
                    .darkmode {
                        background-color: #272623 !important;
                    }

                    /* Custom Dark Mode Font Colors */
                    h1,
                    h2,
                    h3,
                    h4,
                    h5,
                    h6,
                    p,
                    span,
                    a,
                    b,
                    li {
                        color: #ffffff !important;
                    }

                    /* Custom Dark Mode Text Link Color */
                    .link {
                        color: #91ADD4 !important;
                    }
                }

                [data-ogsc] .light-mode-image {
                    display: none;
                    display: none !important;
                }

                [data-ogsc] .dark-mode-image {
                    display: block !important;
                    width: auto !important;
                    overﬂow: visible !important;
                    ﬂoat: none !important;
                    max-height: inherit !important;
                    max-width: inherit !important;
                    line-height: auto !important;
                    margin-top: 0px !important;
                    visibility: inherit !important;
                }

                @media only screen and (max-width: 550px) {

                    .table-container td,
                    .table-container {
                        text-align: center !important;
                    }
                }

            </style>
        </head>

        <body style="padding: 0; margin: 0 auto; background: #fff;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width: 600px; background: #fff; border: 1px solid #e9e9e9;" width="600">
                <tbody>
                    <tr pardot-repeatable="" style="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td style="padding: 15px 0 10px;vertical-align: middle;">
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="vertical-align: middle;">
                                                            <table border="0" cellpadding="0" cellspacing="0" class="table-container" style="width:100%;vertical-align: middle;" width="100%">
                                                                <tbody class="table-body">
                                                                    <tr class="table-row">
                                                                        <td class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle;">
                                                                            <table border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="vertical-align: middle;font-family: Arial, sans-serif, 'Open Sans';color: #0a1626;font-size: 12px;line-height: 140%;text-align: center;padding: 8px 0;mso-line-height-rule: exactly;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                            <div pardot-region="" class=""><img src="https://raw.githubusercontent.com/monetree/help/master/logo-black-h.png" width="140"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                        <td class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle;">
                                                                            <table align="right" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="vertical-align: middle; padding: 20px 0px;">
                                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td>
                                                                                                            <table border="0" cellpadding="0" cellspacing="0" class="button">
                                                                                                                <tbody>
                                                                                                                    <tr>
                                                                                                                        <td style="background:transparent;color: #282a2f;font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 600;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                                                            <div pardot-region="" class="">Create Account</div>
                                                                                                                        </td>
                                                                                                                    </tr>
                                                                                                                </tbody>
                                                                                                            </table>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" bgcolor="#282a2f" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td style="padding: 15px 0;border-bottom: none;border-top: none;">
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="vertical-align: middle;font-family: Arial, sans-serif, 'Open Sans';color: #0a1626;font-size: 12px;line-height: 140%;line-height: 16px;text-align: center;border-collapse: collapse;mso-line-height-rule: exactly;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">&nbsp;</td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td>
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 15px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;text-align: center;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                            <div pardot-region="" class="">
                                                                <h1>Welcome to CGAfrica</h1><br>
                                                                <p><strong>Providing a nbirdge between artist and Opportunities</strong><br>&nbsp;</p>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td>
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td>
                                                            <table border="0" cellpadding="0" cellspacing="0" class="table-container" style="width:100%;" width="100%">
                                                                <tbody class="table-body">
                                                                    <tr class="table-row">
                                                                        <th class="col-md-4" style="font-weight: normal;text-align: center;vertical-align: top;width: 183px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth" style="">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td class="mob-pb-25">
                                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="button-white">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td style="background: #F26522;color: #fff;font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 500;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                                            <div pardot-region="" class=""><a href="linkhere" style="color: #fff !important; text-decoration: none !important">GO TO CGAFRICA</a></div>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </th>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">&nbsp;</td>
                    </tr>

                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td style="background: #F0F2F5;">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td>
                                            <table bgcolor="#fff" align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;background: #fff;" width="550">
                                                <tbody>
                                                    <tr pardot-repeatable="" style="" class="">
                                                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                        <td style="color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 15px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;text-align: center;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;padding-left: 10px;padding-right: 10px;">
                                                            <div pardot-region="" class="">
                                                                <h1>Upload your artworks</h1><br>

                                                                <p>upload your works on CGAfrica to showcase your talent to our community if thriving artist<br>&nbsp;</p>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td>
                                                            <table border="0" cellpadding="0" cellspacing="0" class="table-container" style="width:100%;" width="100%">
                                                                <tbody class="table-body">
                                                                    <tr class="table-row">
                                                                        <th class="col-md-4" style="font-weight: normal;text-align: center;vertical-align: top;width: 183px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth" style="">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td class="mob-pb-25">
                                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="button-white">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td style="background: #F26522;color: #fff;font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 500;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                                            <div pardot-region="" class=""><a href="secondlink" style="color: #fff !important; text-decoration: none !important">UPLOAD YOUR WORK NOW</a></div>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </th>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    <tr pardot-repeatable="" style="" class="">
                                                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">&nbsp;</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                    </tr>
                
                </tbody>
            </table>
        </body>
        </html>


    """

    return BODY_HTML


def comments_email_template():
    BODY_HTML = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http:/i/www.w3.org/1999/xhtml">

        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta name="x-apple-disable-message-reformatting">
            <meta name="color-scheme" content="light dark">
            <meta name="supported-color-schemes" content="light dark">
            <meta property="og:title" contifent="CGAfrica- Comment Notification">
            <title>CGAfrica- Comment Notification</title>
            <style type="text/css">
                :root {
                    color-scheme: light dark;
                    supported-color-schemes: light dark;
                }

                html {
                    width: 100%;
                    margin: 0;
                    padding: 0;
                }

                body {
                    -webkit-text-size-adjust: none;
                    -ms-text-size-adjust: none;
                    margin: 0;
                    padding: 0;
                    color: #0a1626;
                    font-size: 14px;
                    line-height: 140%;
                }

                table {
                    border-spacing: 0;
                    border-collapse: collapse;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                }

                table td {
                    border-spacing: 0;
                    border-collapse: collapse;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                }

                a {
                    color: #1D9AD6;
                    text-decoration: none;
                }

                a:hover {
                    text-decoration: underline;
                }

                img,
                a img,
                a {
                    outline: none;
                    border: none;
                }

                .button a {
                    color: #0a1626 !important;
                    text-decoration: none;
                }

                .button-white a {
                    color: #ffffff;
                    text-decoration: none;
                }

                h1 {
                    font-size: 25px;
                    line-height: 110%;
                    margin: 0 0 12px;
                }

                h2 {
                    font-size: 20px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                h3 {
                    font-size: 18px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                h4 {
                    font-size: 15px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                p {
                    margin: 0 0 10px;
                }

                ul {
                    padding-left: 17px;
                    margin: 0 0 10px;
                }

                [style*="Open Sans"] {
                    font-family: Arial, sans-serif 'Open Sans',  !important;
                }

                @media only screen and (max-width: 600px) {
                    img {
                        max-width: 100% !important;
                        height: auto !important;
                    }

                    .fullwindow-img img,
                    .table-big-image img {
                        width: 100% !important;
                        max-width: 100% !important;
                        height: auto !important;
                    }

                    .table-container,
                    .table-body,
                    .table-row,
                    .col-md-8,
                    .col-md-6,
                    .col-md-4 {
                        display: block !important;
                        padding-left: 0 !important;
                        padding-right: 0 !important;
                        width: 100% !important;
                    }

                    .table600,
                    .table-mob-fullwidth {
                        width: 100% !important;
                    }

                    .mob-pb-25 {
                        padding-bottom: 25px !important;
                        text-align: center !important;
                    }

                    .mob-pb-15 {
                        padding-bottom: 15px !important;
                        text-align: center !important;
                    }

                    .table-inner {
                        width: 94% !important;
                        text-align: center !important;
                    }

                    .spacer {
                        height: 20px !important;
                    }

                    .mob-center,
                    .mobile-img,
                    .table-mob-fullwidth,
                    .table-inner td {
                        text-align: center !important;
                    }

                    .button,
                    .button-white {
                        margin: 0 auto !important;
                    }

                }

                /* Custom Dark Mode Font Colors */
                [data-ogsc] h1,
                [data-ogsc] h2,
                [data-ogsc] h3,
                [data-ogsc] h4,
                [data-ogsc] h5,
                [data-ogsc] h6,
                [data-ogsc] p,
                [data-ogsc] span,
                [data-ogsc] a,
                [data-ogsc] b,
                [data-ogsc] li {
                    color: #ffffff !important;
                }
            

                /* Custom Dark Mode Text Link Color */
                [data-ogsc] .link {
                    color: #91ADD4 !important;
                }

                @media (prefers-color-scheme: dark) {

                    /* Shows Dark Mode-Only Content, Like Images */
                    .dark-img {
                        display: block !important;
                        width: auto !important;
                        overflow: visible !important;
                        float: none !important;
                        max-height: inherit !important;
                        max-width: inherit !important;
                        line-height: auto !important;
                        margin-top: 0px !important;
                        visibility: inherit !important;
                    }

                    /* Hides Light Mode-Only Content, Like Images */
                    .light-img {
                        display: none;
                        display: none !important;
                    }

                    /* Custom Dark Mode Background Color */
                    .darkmode {
                        background-color: #272623 !important;
                    }

                    /* Custom Dark Mode Font Colors */
                    h1,
                    h2,
                    h3,
                    h4,
                    h5,
                    h6,
                    p,
                    span,
                    a,
                    b,
                    li {
                        color: #ffffff !important;
                    }

                    /* Custom Dark Mode Text Link Color */
                    .link {
                        color: #91ADD4 !important;
                    }
                }

                [data-ogsc] .light-mode-image {
                    display: none;
                    display: none !important;
                }

                [data-ogsc] .dark-mode-image {
                    display: block !important;
                    width: auto !important;
                    overﬂow: visible !important;
                    ﬂoat: none !important;
                    max-height: inherit !important;
                    max-width: inherit !important;
                    line-height: auto !important;
                    margin-top: 0px !important;
                    visibility: inherit !important;
                }

                @media only screen and (max-width: 550px) {

                    .table-container td,
                    .table-container {
                        text-align: center !important;
                    }
                }

            </style>
        </head>

        <body  style="padding: 0; margin: 0 auto; background: #fff;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width: 600px; background: #fff; border: 1px solid #e9e9e9;" width="600">
                <tbody>
                    <tr pardot-repeatable="" style="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td style="padding: 15px 0 10px;vertical-align: middle;">
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="vertical-align: middle;">
                                                            <table border="0" cellpadding="0" cellspacing="0" class="table-container" style="width:100%;vertical-align: middle;" width="100%">
                                                                <tbody class="table-body">
                                                                    <tr class="table-row">
                                                                        <td class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle;">
                                                                            <table border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="vertical-align: middle;font-family: Arial, sans-serif, 'Open Sans';color: #0a1626;font-size: 12px;line-height: 140%;text-align: center;padding: 8px 0;mso-line-height-rule: exactly;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                            <div pardot-region="" class=""><img src="https://github.com/monetree/help/blob/master/logo-black-h.png" width="140"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                        <td class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle;">
                                                                            <table align="right" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="vertical-align: middle; padding: 20px 0px;">
                                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td>
                                                                                                            <table border="0" cellpadding="0" cellspacing="0" class="button">
                                                                                                                <tbody>
                                                                                                                    <tr>
                                                                                                                        <td style="background:transparent;color: #282a2f;font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 600;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                                                            <div pardot-region="" class="">Comment</div>
                                                                                                                        </td>
                                                                                                                    </tr>
                                                                                                                </tbody>
                                                                                                            </table>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" bgcolor="#282a2f" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td style="padding: 15px 0;border-bottom: none;border-top: none;">
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="vertical-align: middle;font-family: Arial, sans-serif, 'Open Sans';color: #0a1626;font-size: 12px;line-height: 140%;line-height: 16px;text-align: center;border-collapse: collapse;mso-line-height-rule: exactly;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">&nbsp;</td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td>
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:56px;" width="56">
                                                <tbody>
                                                    <tr>
                                                        <td style="border-radius: 50px;
            color: #fff;
            border:1px solid #707070;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
            font-family: Arial, sans-serif, 'Open Sans';
            font-size: 14px;
            font-weight: 550;
            line-height: 140%;
            mso-line-height-rule: exactly;
            padding: 12px 14.5px;
            ms-text-size-adjust: none;
            -webkit-text-size-adjust: none;
            mso-line-height-rule: exactly;">
                                                            <div pardot-region="" class="">
                                                                <img src="profilepichere" width="50">
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td>
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="padding-top:10px; color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 15px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;text-align: center;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                            <div pardot-region="" class="">
                                                                <h1>usernamehere commented on your artwork</h1><br>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">&nbsp;</td>
                    </tr>

                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                    </tr>
                    <tr pardot-repeatable="">
                        <td style="background: #F0F2F5;">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>

                                        <td background="#F0F2F5">

                                            <table border="0" align="center" cellpadding="0" cellspacing="0" class="table-inner" width="550" style="background:#fff">
                                                <tbody>
                                                    <tr pardot-repeatable="" style="" class="">
                                                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">&nbsp;</td>
                                                    </tr>
                                                    <tr class="table-row">
                                                        <th class="col-md-6 mob-pb-30" style="font-weight: normal; text-align: center; vertical-align: top; width: 200px;" width="200">
                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth" width="200">
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="side-image mob-pb-25" style="font-size: 2px; line-height: 4px;">
                                                                            <div pardot-region=""><img alt="" height="150" src="thumbhere" width="150"></div>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                        <th class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle; width: 250px;" width="300">
                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" width="300">
                                                                <tbody>
                                                                    <tr pardot-repeatable="">
                                                                        <td style=" color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 15px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                                            <div pardot-region="" class="">
                                                                                <h1>titlehere</h1>

                                                                            </div>
                                                                        </td>

                                                                    </tr>
                                                                    <tr>
                                                                        <td style="color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 14px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                            <div pardot-region="" class="">
                                                                                <p>upload your works on CGAfrica to showcase your talent to our community if thriving artist</p>
                                                                                <p><b>commentcounthere comment(s)</b></p><br>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr pardot-repeatable="">
                                                                        <td>
                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="button-white">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="background: #F26522;color: #fff !important; font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 500;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                            <div pardot-region="" class=""><a style="color: #fff !important; text-decoration:none !important;" href="frontendoriginhere" style="">JOIN THE CONVERSATION</a></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    <tr pardot-repeatable="" style="" class="">
                                                                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">&nbsp;</td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>

                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                    </tr>

                </tbody>
            </table>
        </body>

        </html>

    """
    return BODY_HTML


def likes_email_template():
    BODY_HTML = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http:/i/www.w3.org/1999/xhtml">

        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta name="x-apple-disable-message-reformatting">
            <meta name="color-scheme" content="light dark">
            <meta name="supported-color-schemes" content="light dark">
            <meta property="og:title" contifent="CGAfrica- Like Notification">
            <title>CGAfrica- Like Notification</title>
            <style type="text/css">
                :root {
                    color-scheme: light dark;
                    supported-color-schemes: light dark;
                }

                html {
                    width: 100%;
                    margin: 0;
                    padding: 0;
                }

                body {
                    -webkit-text-size-adjust: none;
                    -ms-text-size-adjust: none;
                    margin: 0;
                    padding: 0;
                    color: #0a1626;
                    font-size: 14px;
                    line-height: 140%;
                }

                table {
                    border-spacing: 0;
                    border-collapse: collapse;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                }

                table td {
                    border-spacing: 0;
                    border-collapse: collapse;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                }

                a {
                    color: #1D9AD6;
                    text-decoration: none;
                }

                a:hover {
                    text-decoration: underline;
                }

                img,
                a img,
                a {
                    outline: none;
                    border: none;
                }

                .button a {
                    color: #0a1626 !important;
                    text-decoration: none;
                }

                .button-white a {
                    color: #ffffff;
                    text-decoration: none;
                }

                h1 {
                    font-size: 25px;
                    line-height: 110%;
                    margin: 0 0 12px;
                }

                h2 {
                    font-size: 20px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                h3 {
                    font-size: 18px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                h4 {
                    font-size: 15px;
                    line-height: 110%;
                    margin: 0 0 9px;
                }

                p {
                    margin: 0 0 10px;
                }

                ul {
                    padding-left: 17px;
                    margin: 0 0 10px;
                }

                [style*="Open Sans"] {
                    font-family: Arial, sans-serif 'Open Sans',  !important;
                }

                @media only screen and (max-width: 600px) {
                    img {
                        max-width: 100% !important;
                        height: auto !important;
                    }

                    .fullwindow-img img,
                    .table-big-image img {
                        width: 100% !important;
                        max-width: 100% !important;
                        height: auto !important;
                    }

                    .table-container,
                    .table-body,
                    .table-row,
                    .col-md-8,
                    .col-md-6,
                    .col-md-4 {
                        display: block !important;
                        padding-left: 0 !important;
                        padding-right: 0 !important;
                        width: 100% !important;
                    }

                    .table600,
                    .table-mob-fullwidth {
                        width: 100% !important;
                    }

                    .mob-pb-25 {
                        padding-bottom: 25px !important;
                        text-align: center !important;
                    }

                    .mob-pb-15 {
                        padding-bottom: 15px !important;
                        text-align: center !important;
                    }

                    .table-inner {
                        width: 94% !important;
                        text-align: center !important;
                    }

                    .spacer {
                        height: 20px !important;
                    }

                    .mob-center,
                    .mobile-img,
                    .table-mob-fullwidth,
                    .table-inner td {
                        text-align: center !important;
                    }

                    .button,
                    .button-white {
                        margin: 0 auto !important;
                    }

                }

                /* Custom Dark Mode Font Colors */
                [data-ogsc] h1,
                [data-ogsc] h2,
                [data-ogsc] h3,
                [data-ogsc] h4,
                [data-ogsc] h5,
                [data-ogsc] h6,
                [data-ogsc] p,
                [data-ogsc] span,
                [data-ogsc] a,
                [data-ogsc] b,
                [data-ogsc] li {
                    color: #ffffff !important;
                }

                /* Custom Dark Mode Text Link Color */
                [data-ogsc] .link {
                    color: #91ADD4 !important;
                }

                @media (prefers-color-scheme: dark) {

                    /* Shows Dark Mode-Only Content, Like Images */
                    .dark-img {
                        display: block !important;
                        width: auto !important;
                        overflow: visible !important;
                        float: none !important;
                        max-height: inherit !important;
                        max-width: inherit !important;
                        line-height: auto !important;
                        margin-top: 0px !important;
                        visibility: inherit !important;
                    }

                    /* Hides Light Mode-Only Content, Like Images */
                    .light-img {
                        display: none;
                        display: none !important;
                    }

                    /* Custom Dark Mode Background Color */
                    .darkmode {
                        background-color: #272623 !important;
                    }

                    /* Custom Dark Mode Font Colors */
                    h1,
                    h2,
                    h3,
                    h4,
                    h5,
                    h6,
                    p,
                    span,
                    a,
                    b,
                    li {
                        color: #ffffff !important;
                    }

                    /* Custom Dark Mode Text Link Color */
                    .link {
                        color: #91ADD4 !important;
                    }
                }

                [data-ogsc] .light-mode-image {
                    display: none;
                    display: none !important;
                }

                [data-ogsc] .dark-mode-image {
                    display: block !important;
                    width: auto !important;
                    overﬂow: visible !important;
                    ﬂoat: none !important;
                    max-height: inherit !important;
                    max-width: inherit !important;
                    line-height: auto !important;
                    margin-top: 0px !important;
                    visibility: inherit !important;
                }

                @media only screen and (max-width: 50px) {

                    .table-container td,
                    .table-container {
                        text-align: center !important;
                    }
                }

            </style>
        </head>

        <body style="padding: 0; margin: 0 auto; background: #fff;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width: 600px; background: #fff; border: 1px solid #e9e9e9;" width="600">
                <tbody>
                    <tr pardot-repeatable="" style="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td style="padding: 15px 0 10px;vertical-align: middle;">
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="vertical-align: middle;">
                                                            <table border="0" cellpadding="0" cellspacing="0" class="table-container" style="width:100%;vertical-align: middle;" width="100%">
                                                                <tbody class="table-body">
                                                                    <tr class="table-row">
                                                                        <td class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle;">
                                                                            <table border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="vertical-align: middle;font-family: Arial, sans-serif, 'Open Sans';color: #0a1626;font-size: 12px;line-height: 140%;text-align: center;padding: 8px 0;mso-line-height-rule: exactly;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                            <div pardot-region="" class=""><img src="https://github.com/monetree/help/blob/master/logo-black-h.png" width="140"></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                        <td class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle;">
                                                                            <table align="right" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="vertical-align: middle; padding: 20px 0px;">
                                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td>
                                                                                                            <table border="0" cellpadding="0" cellspacing="0" class="button">
                                                                                                                <tbody>
                                                                                                                    <tr>
                                                                                                                        <td style="background: transparent;color: #282a2f;font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 600;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                                                            <div pardot-region="" class="">Like</div>
                                                                                                                        </td>
                                                                                                                    </tr>
                                                                                                                </tbody>
                                                                                                            </table>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </tbody>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" bgcolor="#282a2f" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td style="padding: 15px 0;border-bottom: none;border-top: none;">
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="vertical-align: middle;font-family: Arial, sans-serif, 'Open Sans';color: #0a1626;font-size: 12px;line-height: 140%;line-height: 16px;text-align: center;border-collapse: collapse;mso-line-height-rule: exactly;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">

                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">&nbsp;</td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td>
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:56px;" width="56">
                                                <tbody>
                                                    <tr>
                                                        <td style="border-radius: 50px; color: #fff; border:1px solid #707070; display: inline-block; margin: 0px auto; text-align: center; font-family: Arial, sans-serif, 'Open Sans'; font-size: 14px; font-weight: 550; line-height: 140%; mso-line-height-rule: exactly; padding: 12px 14.5px; ms-text-size-adjust: none; -webkit-text-size-adjust: none;mso-line-height-rule: exactly;">
                                                            <div pardot-region="" class="">
                                                                <img src="profilepichere" width="50">
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>
                                        <td>
                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" style="width:550px;" width="550">
                                                <tbody>
                                                    <tr>
                                                        <td style="padding-top:10px; color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 15px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;text-align: center;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                            <div pardot-region="" class="">
                                                                <h1>usernamehere likes on your artwork</h1><br>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">&nbsp;</td>
                    </tr>

                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                    </tr>
                    <tr pardot-repeatable="">
                        <td style="background: #F0F2F5;">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table600" style="width:600px;" width="600">
                                <tbody>
                                    <tr>

                                        <td background="#F0F2F5">

                                            <table border="0" align="center" cellpadding="0" cellspacing="0" class="table-inner" width="550" style="background:#fff">
                                                <tbody>
                                                    <tr pardot-repeatable="" style="" class="">
                                                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">&nbsp;</td>
                                                    </tr>
                                                    <tr class="table-row">
                                                        <th class="col-md-6 mob-pb-30" style="font-weight: normal; text-align: center; vertical-align: top; width: 200px;" width="200">
                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-mob-fullwidth" width="200">
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="side-image mob-pb-25" style="font-size: 2px; line-height: 4px;">
                                                                            <div pardot-region=""><img alt="" height="150" src="thumbhere" width="150"></div>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                        <th class="col-md-6" style="font-weight: normal; text-align: left; vertical-align: middle; width: 250px;" width="300">
                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="table-inner" width="300">
                                                                <tbody>
                                                                    <tr pardot-repeatable="">
                                                                        <td style=" color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 15px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;mso-line-height: exactly;  -webkit-text-size-adjust: none;  text-size-adjust: none;">
                                                                            <div pardot-region="" class="">
                                                                                <h1>titlehere</h1>

                                                                            </div>
                                                                        </td>

                                                                    </tr>
                                                                    <tr>
                                                                        <td style="color: #0a1626;font-family: Arial, sans-serif, 'Open Sans';font-size: 14px;line-height: 140%;line-height: 20px;mso-line-height-rule: exactly;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                            <div pardot-region="" class="">
                                                                                <p>upload your works on CGAfrica to showcase your talent to our community if thriving artist</p>
                                                                                <p><b>likecounthere like(s)</b></p><br>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr pardot-repeatable="">
                                                                        <td>
                                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="button-white">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="background: #F26522;color: #fff;font-family: Arial, sans-serif, 'Open Sans';font-size: 16px;font-weight: normal;font-weight: 500;line-height: 17px;mso-line-height-rule: exactly;padding: 12px 20px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">
                                                                                            <div pardot-region="" class=""><a href="frontendoriginhere" style="color:#fff !important; text-decoration: none !important;">JOIN THE CONVERSATION</a></div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    <tr pardot-repeatable="" style="" class="">
                                                                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;">&nbsp;</td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </th>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>

                    <tr pardot-repeatable="" style="" class="">
                        <td class="spacer" height="35" style="font-size: 10px;line-height: 15px;mso-line-height-rule: exactly;height: 35px;mso-line-height: exactly;-webkit-text-size-adjust: none;text-size-adjust: none;background: #F0F2F5;">&nbsp;</td>
                    </tr>

                </tbody>
            </table>
        </body>

        </html>

    """
    return BODY_HTML


def reset_password_email_template():
    BODY_HTML = """ 
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http:/i/www.w3.org/1999/xhtml">
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta name="x-apple-disable-message-reformatting" />
            <meta name="color-scheme" content="light dark" />
            <meta name="supported-color-schemes" content="light dark" />
            <meta property="og:title" contifent="CGAfrica- Verify Email" />
            <title>CGAfrica- Verify Email</title>
            <style type="text/css">
            @import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap");

            :root {
                color-scheme: light dark;
                supported-color-schemes: light dark;
            }

            html {
                width: 100%;
                margin: 0;
                padding: 0;
            }

            body {
                -webkit-text-size-adjust: none;
                -ms-text-size-adjust: none;
                margin: 0;
                padding: 0;
                color: #0a1626;
                font-size: 14px;
                line-height: 140%;
            }

            table {
                border-spacing: 0;
                border-collapse: collapse;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }

            table td {
                border-spacing: 0;
                border-collapse: collapse;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }

            a {
                color: #1d9ad6;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }

            img,
            a img,
            a {
                outline: none;
                border: none;
            }

            .button a {
                color: #0a1626 !important;
                text-decoration: none;
            }

            .button-white a {
                color: #ffffff;
                text-decoration: none;
            }

            h1 {
                font-size: 25px;
                line-height: 110%;
                margin: 0 0 12px;
            }

            h2 {
                font-size: 20px;
                line-height: 110%;
                margin: 0 0 9px;
            }

            h3 {
                font-size: 18px;
                line-height: 110%;
                margin: 0 0 9px;
            }

            h4 {
                font-size: 15px;
                line-height: 110%;
                margin: 0 0 9px;
            }

            p {
                margin: 0 0 10px;
            }

            ul {
                padding-left: 17px;
                margin: 0 0 10px;
            }

            [style*="Open Sans"] {
                font-family: Arial, sans-serif "Open Sans" !important;
            }

            @media only screen and (max-width: 600px) {
                img {
                max-width: 100% !important;
                height: auto !important;
                }

                .fullwindow-img img,
                .table-big-image img {
                width: 100% !important;
                max-width: 100% !important;
                height: auto !important;
                }

                .table-container,
                .table-body,
                .table-row,
                .col-md-8,
                .col-md-6,
                .col-md-4 {
                display: block !important;
                padding-left: 0 !important;
                padding-right: 0 !important;
                width: 100% !important;
                }

                .table600,
                .table-mob-fullwidth {
                width: 100% !important;
                }

                .mob-pb-25 {
                padding-bottom: 25px !important;
                text-align: center !important;
                }

                .mob-pb-15 {
                padding-bottom: 15px !important;
                text-align: center !important;
                }

                .table-inner {
                width: 94% !important;
                }

                .spacer {
                height: 20px !important;
                }

                .mob-center,
                .mobile-img,
                .table-mob-fullwidth,
                .table-inner td {
                text-align: center !important;
                }

                .button,
                .button-white {
                margin: 0 auto !important;
                }
            }

            /* Custom Dark Mode Font Colors */
            [data-ogsc] h1,
            [data-ogsc] h2,
            [data-ogsc] h3,
            [data-ogsc] h4,
            [data-ogsc] h5,
            [data-ogsc] h6,
            [data-ogsc] p,
            [data-ogsc] span,
            [data-ogsc] a,
            [data-ogsc] b,
            [data-ogsc] li {
                color: #ffffff !important;
            }

            /* Custom Dark Mode Text Link Color */
            [data-ogsc] .link {
                color: #91add4 !important;
            }

            @media (prefers-color-scheme: dark) {
                /* Shows Dark Mode-Only Content, Like Images */
                .dark-img {
                display: block !important;
                width: auto !important;
                overflow: visible !important;
                float: none !important;
                max-height: inherit !important;
                max-width: inherit !important;
                line-height: auto !important;
                margin-top: 0px !important;
                visibility: inherit !important;
                }

                /* Hides Light Mode-Only Content, Like Images */
                .light-img {
                display: none;
                display: none !important;
                }

                /* Custom Dark Mode Background Color */
                .darkmode {
                background-color: #272623 !important;
                }

                /* Custom Dark Mode Font Colors */
                h1,
                h2,
                h3,
                h4,
                h5,
                h6,
                p,
                span,
                a,
                b,
                li {
                color: #ffffff !important;
                }

                /* Custom Dark Mode Text Link Color */
                .link {
                color: #91add4 !important;
                }
            }

            [data-ogsc] .light-mode-image {
                display: none;
                display: none !important;
            }

            [data-ogsc] .dark-mode-image {
                display: block !important;
                width: auto !important;
                overﬂow: visible !important;
                ﬂoat: none !important;
                max-height: inherit !important;
                max-width: inherit !important;
                line-height: auto !important;
                margin-top: 0px !important;
                visibility: inherit !important;
            }

            @media only screen and (max-width: 550px) {
                .table-container td,
                .table-container {
                text-align: center !important;
                }
            }
            </style>
        </head>

        <body style="padding: 0; margin: 0 auto; background: #fff">
            <table
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            class="table600"
            style="width: 600px; background: #fff; border: 1px solid #e9e9e9"
            width="600"
            >
            <tbody>
                <tr pardot-repeatable="" style="">
                <td>
                    <table
                    align="center"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="table600"
                    style="width: 600px"
                    width="600"
                    >
                    <tbody>
                        <tr>
                        <td style="padding: 15px 0 10px; vertical-align: middle">
                            <table
                            align="center"
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            class="table-inner"
                            style="width: 550px"
                            width="550"
                            >
                            <tbody>
                                <tr>
                                <td style="vertical-align: middle">
                                    <table
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    class="table-container"
                                    style="width: 100%; vertical-align: middle"
                                    width="100%"
                                    >
                                    <tbody class="table-body">
                                        <tr class="table-row">
                                        <td
                                            class="col-md-6"
                                            style="
                                            font-weight: normal;
                                            text-align: left;
                                            vertical-align: middle;
                                            "
                                        >
                                            <table
                                            border="0"
                                            cellpadding="0"
                                            cellspacing="0"
                                            class="table-mob-fullwidth"
                                            >
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="
                                                    vertical-align: middle;
                                                    font-family: Arial, sans-serif,
                                                        'Open Sans';
                                                    color: #0a1626;
                                                    font-size: 12px;
                                                    line-height: 140%;
                                                    text-align: center;
                                                    padding: 8px 0;
                                                    mso-line-height-rule: exactly;
                                                    mso-line-height: exactly;
                                                    -webkit-text-size-adjust: none;
                                                    text-size-adjust: none;
                                                    "
                                                >
                                                    <div pardot-region="" class="">
                                                    <img
                                                        src="https://raw.githubusercontent.com/monetree/help/master/logo-black-h.png"
                                                        width="140"
                                                    />
                                                    </div>
                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </td>
                                        <td
                                            class="col-md-6"
                                            style="
                                            font-weight: normal;
                                            text-align: left;
                                            vertical-align: middle;
                                            "
                                        >
                                            <table
                                            align="right"
                                            border="0"
                                            cellpadding="0"
                                            cellspacing="0"
                                            class="table-mob-fullwidth"
                                            >
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="
                                                    vertical-align: middle;
                                                    padding: 20px 0px;
                                                    "
                                                >
                                                    <table
                                                    align="center"
                                                    border="0"
                                                    cellpadding="0"
                                                    cellspacing="0"
                                                    >
                                                    <tbody>
                                                        <tr>
                                                        <td>
                                                            <table
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            class="button"
                                                            >
                                                            <tbody>
                                                                <tr>
                                                                <td
                                                                    style="
                                                                    background: transparent;
                                                                    color: #282a2f;
                                                                    font-family: Arial,
                                                                        sans-serif,
                                                                        'Open Sans';
                                                                    font-size: 16px;
                                                                    font-weight: normal;
                                                                    font-weight: 600;
                                                                    line-height: 17px;
                                                                    mso-line-height-rule: exactly;
                                                                    padding: 12px 20px;
                                                                    mso-line-height: exactly;
                                                                    -webkit-text-size-adjust: none;
                                                                    text-size-adjust: none;
                                                                    "
                                                                >
                                                                    <div
                                                                    pardot-region=""
                                                                    class=""
                                                                    >
                                                                    Password Reset
                                                                    </div>
                                                                </td>
                                                                </tr>
                                                            </tbody>
                                                            </table>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>
                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </td>
                                        </tr>
                                    </tbody>
                                    </table>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </td>
                </tr>
                <tr pardot-repeatable="" style="" class="">
                <td>
                    <table
                    align="center"
                    bgcolor="#282a2f"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="table600"
                    style="width: 600px"
                    width="600"
                    >
                    <tbody>
                        <tr>
                        <td
                            style="
                            padding: 15px 0;
                            border-bottom: none;
                            border-top: none;
                            "
                        >
                            <table
                            align="center"
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            class="table-inner"
                            style="width: 550px"
                            width="550"
                            >
                            <tbody>
                                <tr>
                                <td
                                    style="
                                    vertical-align: middle;
                                    font-family: Arial, sans-serif, 'Open Sans';
                                    color: #0a1626;
                                    font-size: 12px;
                                    line-height: 140%;
                                    line-height: 16px;
                                    text-align: center;
                                    border-collapse: collapse;
                                    mso-line-height-rule: exactly;
                                    mso-line-height: exactly;
                                    -webkit-text-size-adjust: none;
                                    text-size-adjust: none;
                                    "
                                ></td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </td>
                </tr>
                <tr pardot-repeatable="" style="" class="">
                <td
                    class="spacer"
                    height="35"
                    style="
                    font-size: 10px;
                    line-height: 15px;
                    mso-line-height-rule: exactly;
                    height: 35px;
                    mso-line-height: exactly;
                    -webkit-text-size-adjust: none;
                    text-size-adjust: none;
                    "
                >
                    &nbsp;
                </td>
                </tr>
                <tr pardot-repeatable="" style="" class="">
                <td>
                    <table
                    align="center"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="table600"
                    style="width: 600px"
                    width="600"
                    >
                    <tbody>
                        <tr>
                        <td>
                            <table
                            align="center"
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            class="table-inner"
                            style="width: 550px"
                            width="550"
                            >
                            <tbody>
                                <tr>
                                <td
                                    style="
                                    color: ##696a6a;
                                    font-family: Arial, sans-serif, 'Open Sans';
                                    font-size: 15px;
                                    line-height: 140%;
                                    line-height: 20px;
                                    mso-line-height-rule: exactly;
                                    text-align: center;
                                    mso-line-height: exactly;
                                    -webkit-text-size-adjust: none;
                                    text-size-adjust: none;
                                    "
                                >
                                    <div pardot-region="" class="">
                                    <h1 style="color: rgb(27, 27, 27)">
                                        Hi usernamehere
                                    </h1>
                                    <br />
                                    <p style="color: rgb(27, 27, 27)">
                                        We have received a request to reset your
                                        password on CGAfrica<br />
                                        &nbsp;
                                    </p>
                                    </div>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </td>
                </tr>

                <tr pardot-repeatable="" style="" class="">
                <td>
                    <table
                    align="center"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="table600"
                    style="width: 600px"
                    width="600"
                    >
                    <tbody>
                        <tr>
                        <td>
                            <table
                            align="center"
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            class="table-inner"
                            style="width: 550px"
                            width="550"
                            >
                            <tbody>
                                <tr>
                                <td>
                                    <table
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    class="table-container"
                                    style="width: 100%"
                                    width="100%"
                                    >
                                    <tbody class="table-body">
                                        <tr class="table-row">
                                        <th
                                            class="col-md-4"
                                            style="
                                            font-weight: normal;
                                            text-align: center;
                                            vertical-align: top;
                                            width: 183px;
                                            mso-line-height: exactly;
                                            -webkit-text-size-adjust: none;
                                            text-size-adjust: none;
                                            "
                                        >
                                            <table
                                            align="center"
                                            border="0"
                                            cellpadding="0"
                                            cellspacing="0"
                                            class="table-mob-fullwidth"
                                            style="margin-bottom: 10px;"
                                            >
                                            <tbody>
                                                <tr>
                                                <td class="mob-pb-25">
                                                    <table
                                                    align="center"
                                                    border="0"
                                                    cellpadding="0"
                                                    cellspacing="0"
                                                    class="button-white"
                                                    >
                                                    <tbody>
                                                        <tr>
                                                        <td
                                                            style="
                                                            background: #f26522;
                                                            color: #fff;
                                                            font-family: Arial,
                                                                sans-serif, 'Open Sans';
                                                            font-size: 16px;
                                                            font-weight: normal;
                                                            font-weight: 500;
                                                            line-height: 17px;
                                                            mso-line-height-rule: exactly;
                                                            padding: 12px 20px;
                                                            margin-bottom: 20px;
                                                            mso-line-height: exactly;
                                                            -webkit-text-size-adjust: none;
                                                            text-size-adjust: none;
                                                            "
                                                        >
                                                            <div
                                                            pardot-region=""
                                                            class=""
                                                            >
                                                            <a
                                                                style="
                                                                color: #fff;
                                                                text-decoration: none !important;
                                                                "
                                                                href="linkhere"
                                                                >Click here to reset
                                                                password</a
                                                            >
                                                            </div>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>
                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </th>
                                        </tr>
                                    </tbody>
                                    </table>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </td>
                </tr>
            </tbody>
            </table>
        </body>
        </html>

    """
    return BODY_HTML


def contact_email():
    BODY_HTML = """ 
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http:/i/www.w3.org/1999/xhtml">
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta name="x-apple-disable-message-reformatting" />
            <meta name="color-scheme" content="light dark" />
            <meta name="supported-color-schemes" content="light dark" />
            <meta property="og:title" contifent="CGAfrica- Verify Email" />
            <title>CGAfrica- Verify Email</title>
            <style type="text/css">
            @import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap");

            :root {
                color-scheme: light dark;
                supported-color-schemes: light dark;
            }

            html {
                width: 100%;
                margin: 0;
                padding: 0;
            }

            body {
                -webkit-text-size-adjust: none;
                -ms-text-size-adjust: none;
                margin: 0;
                padding: 0;
                color: #0a1626;
                font-size: 14px;
                line-height: 140%;
            }

            table {
                border-spacing: 0;
                border-collapse: collapse;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }

            table td {
                border-spacing: 0;
                border-collapse: collapse;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }

            a {
                color: #1d9ad6;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }

            img,
            a img,
            a {
                outline: none;
                border: none;
            }

            .button a {
                color: #0a1626 !important;
                text-decoration: none;
            }

            .button-white a {
                color: #ffffff;
                text-decoration: none;
            }

            h1 {
                font-size: 25px;
                line-height: 110%;
                margin: 0 0 12px;
            }

            h2 {
                font-size: 20px;
                line-height: 110%;
                margin: 0 0 9px;
            }

            h3 {
                font-size: 18px;
                line-height: 110%;
                margin: 0 0 9px;
            }

            h4 {
                font-size: 15px;
                line-height: 110%;
                margin: 0 0 9px;
            }

            p {
                margin: 0 0 10px;
            }

            ul {
                padding-left: 17px;
                margin: 0 0 10px;
            }

            [style*="Open Sans"] {
                font-family: Arial, sans-serif "Open Sans" !important;
            }

            @media only screen and (max-width: 600px) {
                img {
                max-width: 100% !important;
                height: auto !important;
                }

                .fullwindow-img img,
                .table-big-image img {
                width: 100% !important;
                max-width: 100% !important;
                height: auto !important;
                }

                .table-container,
                .table-body,
                .table-row,
                .col-md-8,
                .col-md-6,
                .col-md-4 {
                display: block !important;
                padding-left: 0 !important;
                padding-right: 0 !important;
                width: 100% !important;
                }

                .table600,
                .table-mob-fullwidth {
                width: 100% !important;
                }

                .mob-pb-25 {
                padding-bottom: 25px !important;
                text-align: center !important;
                }

                .mob-pb-15 {
                padding-bottom: 15px !important;
                text-align: center !important;
                }

                .table-inner {
                width: 94% !important;
                }

                .spacer {
                height: 20px !important;
                }

                .mob-center,
                .mobile-img,
                .table-mob-fullwidth,
                .table-inner td {
                text-align: center !important;
                }

                .button,
                .button-white {
                margin: 0 auto !important;
                }
            }

            /* Custom Dark Mode Font Colors */
            [data-ogsc] h1,
            [data-ogsc] h2,
            [data-ogsc] h3,
            [data-ogsc] h4,
            [data-ogsc] h5,
            [data-ogsc] h6,
            [data-ogsc] p,
            [data-ogsc] span,
            [data-ogsc] a,
            [data-ogsc] b,
            [data-ogsc] li {
                color: #ffffff !important;
            }

            /* Custom Dark Mode Text Link Color */
            [data-ogsc] .link {
                color: #91add4 !important;
            }

            @media (prefers-color-scheme: dark) {
                /* Shows Dark Mode-Only Content, Like Images */
                .dark-img {
                display: block !important;
                width: auto !important;
                overflow: visible !important;
                float: none !important;
                max-height: inherit !important;
                max-width: inherit !important;
                line-height: auto !important;
                margin-top: 0px !important;
                visibility: inherit !important;
                }

                /* Hides Light Mode-Only Content, Like Images */
                .light-img {
                display: none;
                display: none !important;
                }

                /* Custom Dark Mode Background Color */
                .darkmode {
                background-color: #272623 !important;
                }

                /* Custom Dark Mode Font Colors */
                h1,
                h2,
                h3,
                h4,
                h5,
                h6,
                p,
                span,
                a,
                b,
                li {
                color: #ffffff !important;
                }

                /* Custom Dark Mode Text Link Color */
                .link {
                color: #91add4 !important;
                }
            }

            [data-ogsc] .light-mode-image {
                display: none;
                display: none !important;
            }

            [data-ogsc] .dark-mode-image {
                display: block !important;
                width: auto !important;
                overﬂow: visible !important;
                ﬂoat: none !important;
                max-height: inherit !important;
                max-width: inherit !important;
                line-height: auto !important;
                margin-top: 0px !important;
                visibility: inherit !important;
            }

            @media only screen and (max-width: 550px) {
                .table-container td,
                .table-container {
                text-align: center !important;
                }
            }
            </style>
        </head>

        <body style="padding: 0; margin: 0 auto; background: #fff">
            <table
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            class="table600"
            style="width: 600px; background: #fff; border: 1px solid #e9e9e9"
            width="600"
            >
            <tbody>
                <tr pardot-repeatable="" style="">
                <td>
                    <table
                    align="center"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="table600"
                    style="width: 600px"
                    width="600"
                    >
                    <tbody>
                        <tr>
                        <td style="padding: 15px 0 10px; vertical-align: middle">
                            <table
                            align="center"
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            class="table-inner"
                            style="width: 550px"
                            width="550"
                            >
                            <tbody>
                                <tr>
                                <td style="vertical-align: middle">
                                    <table
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    class="table-container"
                                    style="width: 100%; vertical-align: middle"
                                    width="100%"
                                    >
                                    <tbody class="table-body">
                                        <tr class="table-row">
                                        <td
                                            class="col-md-6"
                                            style="
                                            font-weight: normal;
                                            text-align: left;
                                            vertical-align: middle;
                                            "
                                        >
                                            <table
                                            border="0"
                                            cellpadding="0"
                                            cellspacing="0"
                                            class="table-mob-fullwidth"
                                            >
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="
                                                    vertical-align: middle;
                                                    font-family: Arial, sans-serif,
                                                        'Open Sans';
                                                    color: #0a1626;
                                                    font-size: 12px;
                                                    line-height: 140%;
                                                    text-align: center;
                                                    padding: 8px 0;
                                                    mso-line-height-rule: exactly;
                                                    mso-line-height: exactly;
                                                    -webkit-text-size-adjust: none;
                                                    text-size-adjust: none;
                                                    "
                                                >
                                                    <div pardot-region="" class="">
                                                     <img
                                                        src="https://raw.githubusercontent.com/monetree/help/master/logo-black-h.png"
                                                        width="140"
                                                    />re
                                                    </div>
                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </td>
                                        <td
                                            class="col-md-6"
                                            style="
                                            font-weight: normal;
                                            text-align: left;
                                            vertical-align: middle;
                                            "
                                        >
                                            <table
                                            align="right"
                                            border="0"
                                            cellpadding="0"
                                            cellspacing="0"
                                            class="table-mob-fullwidth"
                                            >
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="
                                                    vertical-align: middle;
                                                    padding: 20px 0px;
                                                    "
                                                >
                                                    <table
                                                    align="center"
                                                    border="0"
                                                    cellpadding="0"
                                                    cellspacing="0"
                                                    >
                                                    <tbody>
                                                        <tr>
                                                        <td>
                                                            <table
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            class="button"
                                                            >
                                                            <tbody>
                                                                <tr>
                                                                <td
                                                                    style="
                                                                    background: transparent;
                                                                    color: #282a2f;
                                                                    font-family: Arial,
                                                                        sans-serif,
                                                                        'Open Sans';
                                                                    font-size: 16px;
                                                                    font-weight: normal;
                                                                    font-weight: 600;
                                                                    line-height: 17px;
                                                                    mso-line-height-rule: exactly;
                                                                    padding: 12px 20px;
                                                                    mso-line-height: exactly;
                                                                    -webkit-text-size-adjust: none;
                                                                    text-size-adjust: none;
                                                                    "
                                                                >
                                                                    <div
                                                                    pardot-region=""
                                                                    class=""
                                                                    >
                                                                    namehere
                                                                    </div>
                                                                </td>
                                                                </tr>
                                                            </tbody>
                                                            </table>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>
                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </td>
                                        </tr>
                                    </tbody>
                                    </table>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </td>
                </tr>
                <tr pardot-repeatable="" style="" class="">
                <td>
                    <table
                    align="center"
                    bgcolor="#282a2f"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="table600"
                    style="width: 600px"
                    width="600"
                    >
                    <tbody>
                        <tr>
                        <td
                            style="
                            padding: 15px 0;
                            border-bottom: none;
                            border-top: none;
                            "
                        >
                            <table
                            align="center"
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            class="table-inner"
                            style="width: 550px"
                            width="550"
                            >
                            <tbody>
                                <tr>
                                <td
                                    style="
                                    vertical-align: middle;
                                    font-family: Arial, sans-serif, 'Open Sans';
                                    color: #0a1626;
                                    font-size: 12px;
                                    line-height: 140%;
                                    line-height: 16px;
                                    text-align: center;
                                    border-collapse: collapse;
                                    mso-line-height-rule: exactly;
                                    mso-line-height: exactly;
                                    -webkit-text-size-adjust: none;
                                    text-size-adjust: none;
                                    "
                                ></td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </td>
                </tr>
                <tr pardot-repeatable="" style="" class="">
                <td
                    class="spacer"
                    height="35"
                    style="
                    font-size: 10px;
                    line-height: 15px;
                    mso-line-height-rule: exactly;
                    height: 35px;
                    mso-line-height: exactly;
                    -webkit-text-size-adjust: none;
                    text-size-adjust: none;
                    "
                >
                    &nbsp;
                </td>
                </tr>
                <tr pardot-repeatable="" style="" class="">
                <td>
                    <table
                    align="center"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="table600"
                    style="width: 600px"
                    width="600"
                    >
                    <tbody>
                        <tr>
                        <td>
                            <table
                            align="center"
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            class="table-inner"
                            style="width: 550px"
                            width="550"
                            >
                            <tbody>
                                <tr>
                                <td
                                    style="
                                    color: ##696a6a;
                                    font-family: Arial, sans-serif, 'Open Sans';
                                    font-size: 15px;
                                    line-height: 140%;
                                    line-height: 20px;
                                    mso-line-height-rule: exactly;
                                    text-align: center;
                                    mso-line-height: exactly;
                                    -webkit-text-size-adjust: none;
                                    text-size-adjust: none;
                                    "
                                >
                                    <div pardot-region="" class="">
                                    <h1 style="color: rgb(27, 27, 27)">
                                        emailhere
                                    </h1>
                                    <br />
                                    <p style="color: rgb(27, 27, 27)">
                                        messagehere
                                    </p>
                                    </div>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </td>
                </tr>

                <tr pardot-repeatable="" style="" class="">
                <td>
                    <table
                    align="center"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    class="table600"
                    style="width: 600px"
                    width="600"
                    >
                    <tbody>
                        <tr>
                        <td>
                            <table
                            align="center"
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            class="table-inner"
                            style="width: 550px"
                            width="550"
                            >
                            <tbody>
                                <tr>
                                <td>
                                    <table
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    class="table-container"
                                    style="width: 100%"
                                    width="100%"
                                    >
                                    <tbody class="table-body">
                                        <tr class="table-row">
                                        <th
                                            class="col-md-4"
                                            style="
                                            font-weight: normal;
                                            text-align: center;
                                            vertical-align: top;
                                            width: 183px;
                                            mso-line-height: exactly;
                                            -webkit-text-size-adjust: none;
                                            text-size-adjust: none;
                                            "
                                        >
                                            <table
                                            align="center"
                                            border="0"
                                            cellpadding="0"
                                            cellspacing="0"
                                            class="table-mob-fullwidth"
                                            style="margin-bottom: 10px;"
                                            >
                                            <tbody>
                                                <tr>
                                                <td class="mob-pb-25">
                                                    <table
                                                    align="center"
                                                    border="0"
                                                    cellpadding="0"
                                                    cellspacing="0"
                                                    class="button-white"
                                                    >
                                                    <tbody>
                                                        <tr>
                                                        <td
                                                            style="
                                                            background: #f26522;
                                                            color: #fff;
                                                            font-family: Arial,
                                                                sans-serif, 'Open Sans';
                                                            font-size: 16px;
                                                            font-weight: normal;
                                                            font-weight: 500;
                                                            line-height: 17px;
                                                            mso-line-height-rule: exactly;
                                                            padding: 12px 20px;
                                                            margin-bottom: 20px;
                                                            mso-line-height: exactly;
                                                            -webkit-text-size-adjust: none;
                                                            text-size-adjust: none;
                                                            "
                                                        >
                                                            <div
                                                            pardot-region=""
                                                            class=""
                                                            >
                                                            <a
                                                                style="
                                                                color: #fff;
                                                                text-decoration: none !important;
                                                                "
                                                                >messagehere</a
                                                            >
                                                            </div>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>
                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </th>
                                        </tr>
                                    </tbody>
                                    </table>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </td>
                </tr>
            </tbody>
            </table>
        </body>
        </html>

    """
    return BODY_HTML