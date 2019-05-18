SOURCEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

USER_OTLS="${HOME}/"$(basename ${SOURCEDIR})"/otls"
PROD_HDAS="$( cd ${SOURCEDIR} >/dev/null 2>&1 && cd ../../ && cd hdas && pwd )"

before=`pwd`
cd $USER_OTLS

for f in *.{hda,hdanc}
do
  if [ -f $f ] && [ -f "${PROD_HDAS}/${f}" ]
  then
    echo "Copied" $f "to" "${PROD_HDAS}/${f}"
    cp $f "${PROD_HDAS}/${f}"
  fi
done

cd $before
