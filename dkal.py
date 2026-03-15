import tkinter as tk
from tkinter import ttk
from math import floor

Commission_Rate=0.0112
Color_BG="#1e1e1e"
Color_Panel="#2b2b2b"
Color_Text="#ffffff"
Color_Accent="#00d084"
Color_Entry_BG="#3c3c3c"
Font_Title=("Segoe UI",22,"bold")
Font_Subtitle=("Segoe UI",12, "bold")
Font_Label=("Segoe UI",12)
Font_Input=("Segoe UI",13)
Font_Output=("Segoe UI",16,"bold")

def to_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return "Input Numbers"
    
def format_money(value: float) -> str:
    return f"{value:,.2f}"

def cal_buy_breakeven(buy_price: float) -> tuple[float, float]:
    buy_after = buy_price * (1 + Commission_Rate)
    breakeven_sell = buy_price * (1 + (Commission_Rate * 2))
    return buy_after, breakeven_sell

def cal_sell_breakeven(sell_price: float) -> tuple[float, float]:
    sell_after = sell_price * (1 - Commission_Rate)
    breakeven_buy = sell_price * (1 - (Commission_Rate * 2))
    return sell_after, breakeven_buy

def cal_quantity(amount: float, stock_price: float) -> float:
    total_cost = stock_price * (1 + Commission_Rate)
    quantity = (amount / total_cost)
    return quantity

def label(label: tk.Label) -> None:
    label.configure(bg=Color_Panel, fg=Color_Text, font=Font_Label)

def result(label: tk.Label) -> None:
    label.configure(bg=Color_Panel, fg=Color_Text, font=Font_Output)

def entry(entry: tk.Entry) -> None:
    entry.configure(
        bg=Color_Entry_BG,
        fg=Color_Text,
        insertbackground=Color_Text,
        relief=tk.FLAT,
        font=Font_Input,
    )

def button(button: tk.Button) -> None:
    button.configure(
        bg=Color_Accent,
        fg=Color_Text,
        activebackground=Color_Accent,
        activeforeground=Color_Text,
        relief=tk.FLAT,
        font=Font_Label,
    )

def buy_tab(tab: tk.Frame) -> None:
    tab.columnconfigure(1, weight=1)

    buy_var = tk.StringVar()
    buy_after_var = tk.StringVar(value="Buy Price including Commission: ")
    bes_var = tk.StringVar(value="Break Even Share Price: ")

    label_buy = tk.Label(tab, text="Buy Price: ")
    label_buy.grid(row=0, column=0, sticky="W", padx=(0,8), pady=6)
    label(label_buy)

    entry_buy = tk.Entry(tab, textvariable=buy_var, width=20)
    entry_buy.grid(row=0, column=1, sticky="ew", pady=6)
    entry(entry_buy)

    def on_cal():
        buy_price = to_float(buy_var.get())
        if buy_price is None or buy_price <= 0:
            buy_after_var.set("Enter a valid Buy Price")
            bes_var.set("Enter a valid Buy Price")
            return
        buy_after, breakeven_sell = cal_buy_breakeven(buy_price)
        buy_after_var.set(f'Buy Price including Commission: {format_money(buy_after)}')
        bes_var.set(f'Break Even Share Price: {format_money(breakeven_sell)}')

    btn = tk.Button(tab, text="Calculate", command=on_cal)
    btn.grid(row=1, column=0, columnspan=2, pady=(8,6))
    button(btn)

    result_buy = tk.Label(tab, textvariable=buy_after_var)
    result_buy.grid(row=2, column=0, columnspan=2, sticky="w", pady=4)
    result(result_buy)

    result_bes = tk.Label(tab, textvariable=bes_var)
    result_bes.grid(row=3, column=0, columnspan=2, sticky="w", pady=4)
    result(result_bes)
    
def sell_tab(tab: tk.Frame) -> None:
    tab.columnconfigure(1, weight=1)

    sell_var = tk.StringVar()
    sell_after_var = tk.StringVar(value="Sell Price including Commission: ")
    bes_var = tk.StringVar(value="Break Even Share Price: ")

    label_sell = tk.Label(tab, text="Sell Price: ")
    label_sell.grid(row=0, column=0, sticky="W", padx=(0,8), pady=6)
    label(label_sell)

    entry_sell = tk.Entry(tab, textvariable=sell_var, width=20)
    entry_sell.grid(row=0, column=1, sticky="ew", pady=6)
    entry(entry_sell)

    def on_cal():
        sell_price = to_float(sell_var.get())
        if sell_price is None or sell_price <= 0:
            sell_after_var.set("Enter a valid Sell Price")
            bes_var.set("Enter a valid Sell Price")
            return
        sell_after, breakeven_buy = cal_sell_breakeven(sell_price)
        sell_after_var.set(f'Sell Price including Commission: {format_money(sell_after)}')
        bes_var.set(f'Break Even Share Price: {format_money(breakeven_buy)}')

    btn = tk.Button(tab, text="Calculate", command=on_cal)
    btn.grid(row=1, column=0, columnspan=2, pady=(8,6))
    button(btn)

    result_sell = tk.Label(tab, textvariable=sell_after_var)
    result_sell.grid(row=2, column=0, columnspan=2, sticky="w", pady=4)
    result(result_sell)

    result_bes = tk.Label(tab, textvariable=bes_var)
    result_bes.grid(row=3, column=0, columnspan=2, sticky="w", pady=4)
    result(result_bes)

def build_breakeven_panel(parent: tk.Frame) -> None:
    panel = tk.LabelFrame(
        parent,
        text="Breakeven Calculator",
        bg=Color_Panel,
        fg=Color_Text,
        padx=12,
        pady=12,
        bd=0,
        labelanchor="nw",
        font=Font_Label,
    )
    panel.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
    panel.columnconfigure(0, weight=1)
    panel.rowconfigure(0, weight=1)

    notebook = ttk.Notebook(panel)
    notebook.grid(row=0, column=0, sticky="nsew")

    tab_buy = tk.Frame(notebook, bg=Color_Panel, padx=8, pady=8)
    tab_sell = tk.Frame(notebook, bg=Color_Panel, padx=8, pady=8)
    notebook.add(tab_buy, text="BUY")
    notebook.add(tab_sell, text="SELL")

    buy_tab(tab_buy)
    sell_tab(tab_sell)

def build_quantity_panel(parent: tk.Frame) -> None:
    panel = tk.LabelFrame(
        parent,
        text="Quantity Calculator",
        bg=Color_Panel,
        fg=Color_Text,
        padx=12,
        pady=12,
        bd=0,
        labelanchor="nw",
        font=Font_Label,
    )
    panel.grid(row=0, column=0, sticky="nsew", padx=(8, 0))
    panel.columnconfigure(1, weight=1)

    amount_var = tk.StringVar()
    price_var = tk.StringVar()
    qty_out_var = tk.StringVar(value="Quantity: ")

    label_amount = tk.Label(panel, text="Amount (LKR): ")
    label_amount.grid(row=0, column=0, sticky="w", padx=(0, 8), pady=6)
    label(label_amount)

    entry_amount = tk.Entry(panel, textvariable=amount_var, width=20)
    entry_amount.grid(row=0, column=1, sticky="ew", pady=6)
    entry(entry_amount)

    label_price = tk.Label(panel, text="Stock Price: ")
    label_price.grid(row=1, column=0, sticky="w", padx=(0, 8), pady=6)
    label(label_price)

    entry_price = tk.Entry(panel, textvariable=price_var, width=20)
    entry_price.grid(row=1, column=1, sticky="ew", pady=6)
    entry(entry_price)

    def on_calculate():
        amount = to_float(amount_var.get())
        price = to_float(price_var.get())
        if amount is None or price is None or amount <= 0 or price <= 0:
            qty_out_var.set("Enter valid Amount and Stock Price")
            return
        qty = cal_quantity(amount, price)
        qty_out_var.set(f"Quantity: {qty}")

    btn = tk.Button(panel, text="Calculate", command=on_calculate)
    btn.grid(row=2, column=0, columnspan=2, pady=(8, 6))
    button(btn)

    result_qty = tk.Label(panel, textvariable=qty_out_var)
    result_qty.grid(row=3, column=0, columnspan=2, sticky="w", pady=4)
    result(result_qty)

def build_app(root: tk.Tk) -> None:
    root.title("DKal")
    root.geometry("900x500")
    root.resizable(False, False)
    root.configure(bg=Color_BG)

    style = ttk.Style(root)
    style.theme_use("default")
    style.configure("TNotebook", background=Color_Panel, borderwidth=0)
    style.configure(
        "TNotebook.Tab",
        background=Color_Panel,
        foreground=Color_Text,
        padding=(12, 6),
        font=Font_Label,
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", Color_Entry_BG)],
        foreground=[("selected", Color_Text)],
    )

    header = tk.Label(root, text="DKal", bg=Color_BG, fg=Color_Text, font=Font_Title)
    header.grid(row=0, column=0, sticky="ew", pady=(12, 0))

    subtitle = tk.Label(root, text="Stock Price Toolkit", bg=Color_BG, fg=Color_Text, font=Font_Subtitle)
    subtitle.grid(row=1, column=0, sticky="ew", pady=(0, 12))

    main = tk.Frame(root, bg=Color_BG, padx=12, pady=12)
    main.grid(row=2, column=0, sticky="nsew")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(2, weight=1)

    main.columnconfigure(0, weight=2)
    main.columnconfigure(1, weight=1)
    main.rowconfigure(0, weight=1)

    left = tk.Frame(main, bg=Color_BG)
    right = tk.Frame(main, bg=Color_BG)
    left.grid(row=0, column=0, sticky="nsew")
    right.grid(row=0, column=1, sticky="nsew")
    left.columnconfigure(0, weight=1)
    left.rowconfigure(0, weight=1)
    right.columnconfigure(0, weight=1)
    right.rowconfigure(0, weight=1)

    build_breakeven_panel(left)
    build_quantity_panel(right)

def main() -> None:
    root = tk.Tk()
    build_app(root)
    root.mainloop()

if __name__ == "__main__":
    main()