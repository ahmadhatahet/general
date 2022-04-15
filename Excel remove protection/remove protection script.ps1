# reading password
$password = Get-Content -Path '.\passwords.txt'

$wb_password = $password.Split(":")[1]
$ws_password = $password.Split(":")[3]

# create excel object and disable showing the excel window
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# for each .xlsx file in the current folder remove sheet protection
Get-ChildItem -Path "./" -Filter "*.xlsx" | % {

    # Feedback
    Write-Host "Unlocking $($_.BaseName)"

    $excelfile = $_.FullName

    # open the workbook
    $wb = $excel.Workbooks.Open($excelfile, $false, $false, [Type]::Missing, $wb_password)

    # remove protection from this workbook
    $wb.Unprotect($wb_password)
    $wb.Password = ""

    # remove protection from first worksheet
    $wb.Worksheets(1).Unprotect($ws_password)


    # close the workbook and save the changes
    $wb.Save()
    $wb.Close($true)

}

# Closing excel
$excel.Quit()

# freeing the memory
$null = [System.Runtime.Interopservices.Marshal]::ReleaseComObject($wb)
$null = [System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel)
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()