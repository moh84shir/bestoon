from django.shortcuts import render
from expenses.models import Expense
from incomes.models import Income
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def results_export_pdf(request):
    user = request.user
    incomes = Income.objects.get_by_user(user)
    expenses = Expense.objects.get_by_user(user)
    incomes_list = []
    expense_list = []
    for income in incomes:
        incomes_list.append(income.amount)

    for expense in expenses:
        expense_list.append(expense.amount)

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(60, 800, f"your username  : { user.username } ")
    p.drawString(60, 750, f"your incomes sum : { sum(incomes_list) }")
    p.drawString(60, 700, f"your incomes count : { len(incomes_list) }")
    p.drawString(60, 650, f"your expenses sum : { sum(expense_list) }")
    p.drawString(60, 600, f"your expenses count : {len(expense_list)}")

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='bestoon.pdf')
