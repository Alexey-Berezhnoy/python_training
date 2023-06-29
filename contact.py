class NamesCl:

    def __init__(self, first_name, middle_name, last_name, nickname):
        self.a = first_name
        self.b = middle_name
        self.c = last_name
        self.d = nickname


class CompanyDataCl:
    def __init__(self, company_short_name, company_full_name, company_address):
        self.a = company_short_name
        self.b = company_full_name
        self.c = company_address


class PhonesCl:
    def __init__(self, home_tel, mobile_tel, work_tel, fax):
        self.a = home_tel
        self.b = mobile_tel
        self.c = work_tel
        self.d = fax


class MailsCl:
    def __init__(self, mail01, mail02, mail03):
        self.a = mail01
        self.b = mail02
        self.c = mail03


class HomepageCl:
    def __init__(self, homepage01):
        self.a = homepage01


class MoreInfoCl:
    def __init__(self, additional_address01, additional_phone01, notes):
        self.a = additional_address01
        self.b = additional_phone01
        self.c = notes
